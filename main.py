import os.path
import glob
import logging
import re
from datetime import date, timedelta

import numpy as np
import pandas as pd

from dateparser import parse
from forex_python.converter import CurrencyRates


logging.basicConfig(level=logging.CRITICAL)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

curr_rates = CurrencyRates()
one_day = timedelta(days=1)


class Statement:
    def __init__(self, csv_file: str, year: int, dec_sep: str, thousands_sep: str):
        self.dec_sep = dec_sep
        self.year = year
        self.thousands_sep = thousands_sep
        self.csv_file = csv_file

        self.currency = re.findall(pattern=r'(?<=Revolut-)...(?=-)', string=self.csv_file)[0]
        self.csv = None
        self._load_csv()
        self._starting_balance = None
        self._compute_starting_balance()

    def _load_csv(self):
        # FIXME: Revolut statements flush text in a new line if the maximum length is exceeded. This messes with parsing
        # csv columns:
        #   0: 'Completed Date'
        #   1: 'Description'
        #   2: 'Paid Out (...)'
        #   3: 'Paid In (...)',
        #   4: 'Exchange Out'
        #   5: 'Exchange In'
        #   6: 'Balance (...)'
        #   7: 'Category'
        #   8: 'Notes'

        self.csv = pd.read_csv(filepath_or_buffer=self.csv_file, delimiter=r'\s*;\s*',
                               thousands=self.thousands_sep, decimal=self.dec_sep, dtype={2: np.float64,
                                                                                          3: np.float64,
                                                                                          6: np.float64})

        self.csv.iloc[:, 0] = self.csv.iloc[:, 0].apply(lambda x: parse(x).date())

        if len(self.csv) < 1:
            logger.warning('{} statement has no entries for year {}'.format(self.currency, self.year))
            raise NotImplementedError('Empty statements are not handled and likely to conflict with following code')

        # TODO: check if dates are in ascending order
        # TODO: parse file name to check if the required interval is available
        self.csv = self.csv.loc[[entry_date.year == self.year for entry_date in self.csv.iloc[:, 0]]]

        logger.info('{} statement for {} correctly imported'.format(self.currency, self.year))

    def _compute_starting_balance(self):
        # From first balance of the year (last entry), subtract paid in and add paid out
        self._starting_balance = self.csv.iloc[-1, 6] + \
                                 (0 if np.isnan(self.csv.iloc[-1, 2]) else self.csv.iloc[-1, 2]) - \
                                 (0 if np.isnan(self.csv.iloc[-1, 3]) else self.csv.iloc[-1, 3])

    def get_eoy_balance(self, target_currency: str = 'EUR'):
        logger.info('Computing EOY balance for {}'.format(self.currency))
        return curr_rates.convert(self.currency, target_currency,
                                  self.csv.iloc[0, 6], date(year=self.year, month=12, day=31))

    def get_average_daily_balance(self, target_currency: str = 'EUR'):
        logger.info('Computing average daily balance for {}'.format(self.currency))
        reduced_csv = self.csv.drop_duplicates(subset=[self.csv.columns[0]])
        balance = self._starting_balance
        day = date(year=self.year, month=1, day=1)
        total_daily_balance = 0

        while day <= date(2019, 12, 31) and len(reduced_csv) > 0:

            if day >= reduced_csv.iloc[-1, 0]:
                balance = reduced_csv.iloc[-1, 6]
                reduced_csv = reduced_csv.iloc[:-1, :]

            logger.debug('Balance in {} on {}: {}'.format(day, self.currency, balance))

            total_daily_balance = total_daily_balance + (0 if balance == 0 else
                                                         (balance if self.currency == target_currency else
                                                          curr_rates.convert(self.currency, target_currency, balance,
                                                                             day)))

            day = day + one_day

        return total_daily_balance / ((date(self.year, 12, 31) - date(self.year, 1, 1)).days + 1)


if __name__ == "__main__":
    # User settings
    user_dec_sep = '.'
    user_thousands_sep = ','
    user_year = date.today().year - 2
    user_target_curr = 'EUR'
    statements_path = r""

    # Import list of relevant files
    files = glob.glob(os.path.join(statements_path, "Revolut*.csv"))

    statements = []

    # Parse files
    for file in files:
        logger.info('Importing {}'.format(file))
        statements.append(Statement(file, user_year, user_dec_sep, user_thousands_sep))

    overall_gma = 0
    overall_eoy_balance = 0

    for entry in statements:
        overall_gma = overall_gma + entry.get_average_daily_balance(user_target_curr)
        overall_eoy_balance = overall_eoy_balance + entry.get_eoy_balance(user_target_curr)

    print('Overall EOY balance for {}: {} {}'.format(user_year, overall_eoy_balance, user_target_curr))
    print('Overall average daily balance for {}: {} {}'.format(user_year, overall_gma, user_target_curr))

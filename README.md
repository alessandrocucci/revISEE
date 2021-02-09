# revISEE

Compute the averaged daily balance and the end of year balance for your Revolut account.

Requirements:
* [forex-python](https://pypi.org/project/forex-python/)
* [dateparser](https://pypi.org/project/dateparser/)
* pandas
* numpy
```
usage: python revISEE.py [options]

Compute values required for italian ISEE from Revolut statements

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose
  -p PATH, --path PATH  path to statements path - default: cwd
  -y YEAR, --year YEAR  year for computation - default: 2 years ago
  -c CURR, --curr CURR  target currency - default: EUR
  --decsep DECSEP       decimal separator - default: .
  --thosep THOSEP       thousands separator - default: ,
  --detailed            print balances for each currency

MIT License - Copyright (c) 2021 Pietro Pelizzari
```
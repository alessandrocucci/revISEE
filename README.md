# revISEE

Compute the averaged daily balance and the end of year balance for your Revolut account. 
The implementation follows the algorithms described [here](https://www.agenziaentrate.gov.it/portale/it/web/guest/schede/comunicazioni/integrativa-archivio-dei-rapporti-con-operatori-finanziari/giacenza-media-annua).

The averaged daily balance for the foreign currency accounts is converted in EUR using the daily forex value.
Since the API to retrieve historic forex values is rather slow, allow the algorithm time to execute. 
Activate verbose mode to follow the status.

Remember to set the correct decimal and thousand separators depending on the language set on your phone.

The application has been developed and tested with `python 3.8`

Required packages:
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
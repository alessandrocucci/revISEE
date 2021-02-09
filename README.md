# revISEE

Compute the averaged daily balance and the end of year balance for your Revolut account. 
The implementation follows the algorithms described [here](https://www.agenziaentrate.gov.it/portale/it/web/guest/schede/comunicazioni/integrativa-archivio-dei-rapporti-con-operatori-finanziari/giacenza-media-annua).

The averaged daily balance for the foreign currency accounts is converted in EUR on a daily basis using the daily forex value.
Since the API to retrieve historic forex values is rather slow, allow the algorithm time to execute. 
Activate verbose mode to follow the status.

Feel free to open a new issue for any suggestion you might have or start contributing directly with pull requests.

## How to
Set a python 3.8 environment. If you are not familiar with python, I suggest that you use [Anaconda](https://www.anaconda.com/products/individual#Downloads).

Open a terminal and install the required dependencies (open the Anaconda prompt if you are using Windows).

```
>> pip install numpy pandas dateparser forex-python
```

Collect all your Excel Revolut statement in a single folder and make sure that:
* they cover the relevant period (they can also cover a longer period),
* they have not been renamed `Revolut-[CUR]-*.csv`.

Download the latest [release](https://github.com/pietropelizzari/revISEE/releases/latest) and unpack it. 
Now you can either copy the `revISEE.py` script to the folder containing the statements, or you can use the `-p` path option at run time.

Navigate to the script folder with your terminal and run it with the necessary options. 
Remember to set the correct decimal and thousands separators depending on the language set on your phone.

The command will look something like this:

```
>>> python revISEE.py -p "C:\Users\name\Documents\Revolut" -y 2019 --decsep ',' --thosep '.'
```

Required packages:
* [forex-python](https://pypi.org/project/forex-python/)
* [dateparser](https://pypi.org/project/dateparser/)
* pandas
* numpy

## Help

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

## Disclaimer

**revISEE** is in no way endorsed nor supported by Revolut.

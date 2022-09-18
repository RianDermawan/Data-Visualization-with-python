# problem 
# count data by month of all year in column 'RR' whose that values is greater than 20

# answer
import pandas as pd
import seaborn as sns
from datetime import datetime

# read excel file
dataku = pd.read_excel('dataku.xlsx')

# data view
dataku

# Because in column 'Date' the type data is string, convert type data to sring
dataku['Date'] = pd.to_datetime(dataku['Date'], format = '%d-%m-%Y')

# filter data whose values in column 'RR' is greater than or equals 20
dataku_new = dataku[(dataku['RR'] >= 20)]

# add column year and month
dataku_new['Year'] = pd.DatetimeIndex(dataku_new['Date']).year
dataku_new['Month'] = pd.DatetimeIndex(dataku_new['Date']).month

# update data view
dataku_new

# ghraph by month in all year
sns.countplot(x='Month', data=dataku_new)

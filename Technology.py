import pandas as pd
import os
import requests
import lxml
from pytrends.request import TrendReq

def set_working_directory(directory):
    '''Reads directory as a string argument and changes to desired location'''
    os.chdir(directory)
    print('Directory changed to {}'.format(directory))

def readCSV(file, sep, encoding, error_bad_lines):
    '''Calls Pandas read_csv on file with choice of separator, encoding, and error_bad_lines.'''
    df = pd.read_csv(file, sep=sep, encoding=encoding, error_bad_lines=error_bad_lines)
    return df

def create_unique_list(dataframe, column, sort=False):
    '''Returns a list of unique values in a specified column of dataframe.
       Sorts alphabetically if sort=True (False as default).
    '''
    unique = dataframe[column].unique()
    if sort:
        unique = sorted(unique, key=str.lower)
    return unique

def query_trends(kwlist, timeframe='today 5-y', geo=''):
    '''
    Returns Google trends interest over time data for specified time period and location.
    kwlist: Key-word as a list
    timeframe: e.g. "today 5-m" - Default = last 5 years ("today 5-y")
    geo: e.g. "US" - Default = World ('')
    '''
    pytrends.build_payload(kwlist, timeframe=timeframe, geo=geo)
    df = pytrends.interest_over_time()
    return df

def create_trend_dataframe(dataframe):
    trends = pd.DataFrame()
    empty = []
    if len(df) == 0:
        empty.append()

set_working_directory(r'C:\Users\adebola.oshomoji\Documents\KEYRUS_Bootcamp_November\2017\20171030_erp_be_unzipped')
df = readCSV('technology.csv', sep = ',', encoding='utf-16', error_bad_lines=False)
technology =  create_unique_list(df, 'Name', sort=True)

pytrends = TrendReq(hl='en-US', tz=360)

tech_interest = pd.DataFrame()

kw_list = technology[4:6]
pytrends.build_payload('test', timeframe='today 5-y') #
df = pytrends.interest_over_time() #
print(df)
print(technology[5])
#print(len(technology) - 1)
'''
for tech in technology[0]:
    kw_list = [tech]
    pytrends.build_payload(kw_list, timeframe='today 5-y')
    df = pytrends.interest_over_time()
    df = df.drop('isPartial', axis=1)
    tech_interest = pd.concat([tech_interest, df], axis=1)

print(tech_interest)
'''
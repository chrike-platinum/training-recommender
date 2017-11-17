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
    '''
    Returns a list of unique values in a specified column of dataframe.
    Sorts alphabetically if sort=True (False as default).
    '''
    unique = dataframe[column].unique()
    if sort:
        unique = sorted(unique, key=str.lower)
    return unique

def query_trends(kwlist, timeframe='today 5-y', geo=''):
    '''
    Returns DataFrame of Google trends interest over time for specified time period and location.
    kwlist: Keyword as a list
    timeframe: e.g. "today 5-m" - Default = last 5 years ("today 5-y")
    geo: e.g. "US" - Default = World ('')
    '''
    pytrends.build_payload(kwlist, timeframe=timeframe, geo=geo)
    df = pytrends.interest_over_time()
    return df

def get_weight(kwlist, timeframe='today 5-y', geo=''):
    '''
    Calls query_trends function, which returns a DataFrame of Google Trends data for given keyword (list)
    Calculates weight value based on change in interest within time period
    Params: kwlist - Keyword parameter (list), timeframe - time period for trend data (string), geo - location (string)
    Returns a weight value
    '''
    df = query_trends(kwlist=kwlist, timeframe=timeframe, geo=geo)
    nrow = df.shape[0]

    if nrow == 0:
        weight = 0
    else:
        y1 = df.iloc[1, 0]
        y2 = df.iloc[nrow - 1, 0]
        weight = (y2 - y1) / nrow

        print('tech: ' + str(kwlist[0]) + ', y1: ' + str(y1) + ', y2: ' + str(y2) + ', nrow: ' + str(nrow) + ', weight: ' + str(weight))

    return weight

#def dict_to_csv(dict, orient='index'):
#    df = pd.DataFrame.from_dict(dict, orient=orient)
#    print(df)

set_working_directory(r'C:\Users\adebola.oshomoji\Documents\KEYRUS_Bootcamp_November\2017\20171030_erp_be_unzipped')
df = readCSV('technology.csv', sep = ',', encoding='utf-16', error_bad_lines=False)
technology =  create_unique_list(df, 'Name', sort=True)

pytrends = TrendReq(hl='en-US', tz=360)

tech_weights_dict = {element: get_weight([element]) for element in technology}
#dict_to_csv(tech_weights_dict)

print(tech_weights_dict)

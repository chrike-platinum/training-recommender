import pandas as pd
import os

def setWorkingDirectory(directory):
    '''Reads directory as a string argument and changes to desired location'''
    os.chdir(directory)
    print('Directory changed to {}'.format(directory))

def readCSV(file, sep, encoding, error_bad_lines):
    '''Calls Pandas read_csv with choice of separator, encoding, and error_bad_lines.'''
    df = pd.read_csv(file, sep=sep, encoding=encoding, error_bad_lines=error_bad_lines)
    return df

def createUniqueList(dataframe, column, sort=False):
    '''Returns a list of unique values in a specified column of dataframe.
       Sorts alphabetically if sort=True (False as default).
    '''
    unique = dataframe[column].unique()
    if sort:
        unique = sorted(unique, key=str.lower)
    return unique

setWorkingDirectory(r'C:\Users\adebola.oshomoji\Documents\KEYRUS_Bootcamp_November\2017\20171030_erp_be_unzipped')
df = readCSV('technology.csv', sep = ',', encoding='utf-16', error_bad_lines=False)
technology =  createUniqueList(df, 'Name', sort=True)

print([tech for tech in technology])

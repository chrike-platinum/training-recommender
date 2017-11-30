from Christiaan.csvLoading.CSVLoader import read_csv_tableau
from Christiaan.dataCleaning.dataCleaner import cleanTechColumn
import pandas as pd
import numpy as np

def readTechCSV(filename):
    df = read_csv_tableau(filename, filename)
    df = df[['Employee Number', 'Firstname Firstname', 'Lastname Lastname', 'Level Level', 'Practice Practice', 'Suggested Daily Rate', 'Name Name']]
    df.columns =['Employee Number', 'Firstname', 'Lastname', 'Level', 'Practice', 'Suggested Daily Rate', 'Technology']
    df.sort_values('Employee Number', inplace=True)
    return df


def fixLevels(dataFrame):
    emp_first_names = ['Jean-Francois',
                       'Arnaud',
                       'Vasilij',
                       'Pieter',
                       'Koen',
                       'Faisal',
                       'Gunther',
                       'Philip',
                       'Geoffrey']
    emp_last_names = ['Gigot',
                      'Deflorenne',
                      'Nevlev',
                      'Vandamme',
                      'Dils',
                      'Orakzai',
                      'Hellebaut',
                      'Allegaert',
                      'Moerenhoudt']

    for i in range(len(emp_first_names)):
        f = emp_first_names[i]
        l = emp_last_names[i]
        if f == 'Jean-Francois' and l == 'Gigot':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Director'
        elif f == 'Arnaud' and l == 'Deflorenne':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Partner'
        elif f == 'Vasilij' and l == 'Nevlev':
            dataFrame.drop(dataFrame[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l)].index, axis=0, inplace=True)
        elif f == 'Pieter' and l == 'Vandamme':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Director'
        elif f == 'Koen' and l == 'Dils':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Director'
        elif f == 'Faisal' and l == 'Orakzai':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Senior'
        elif f == 'Gunther' and l == 'Hellebaut':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Senior'
        elif f == 'Philip' and l == 'Allegaert':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Director'
        elif f == 'Geoffrey' and l == 'Moerenhoudt':
            dataFrame.loc[np.logical_and(dataFrame.Firstname == f, dataFrame.Lastname == l),'Level'] = 'Consultant'
    return dataFrame

def cleanTech(dataFrame, techColumnName):
    df = cleanTechColumn(dataFrame, techColumnName)
    df.drop_duplicates(inplace=True)
    df = fixLevels(df)
    return df

def exportDF(dataFrame, fileName, path=''):
    dataFrame.to_csv(path_or_buf=path+fileName, sep=',', index=False)


# Read Tableau csv export
file = r'C:\Users\adebola.oshomoji\PycharmProjects\case-keyrus\tableau_technology_export.csv'
df = readTechCSV(file)

# Clean Technology column values and drop duplicates
df = cleanTech(df, 'Technology')

# Write DataFrame to csv
exportDF(df, 'EmployeeTechnologyData.csv')



__author__ = 'christiaan'
from Christiaan.csvLoading.DataFrameLoader import getTableauData
from Christiaan.dataCleaning.dataCleaner import cleanTechColumn


def getExperienceTechDataSet():
    df = getTableauData('experiences+technology')
    df = df[['Employee Number','Name','Name (dim levelsofexperience.csv)','Name (dim technologycategories.csv)']]
    df.columns = ['employeeNumber','Technology','ExperienceLevel','TechnologyCategory']
    df = df.sort_values('employeeNumber')
    df = cleanTechColumn(df,'Technology')#Data cleaning
    return df

def getListOfTechnologiesAndCats(df,employeeNumber,employeeNrColumnName,technologyColumnName,technologyCatColumnName):
    df[technologyColumnName]=df[technologyColumnName].str.lower()
    dfA =df.loc[df[employeeNrColumnName] == employeeNumber, [technologyColumnName,technologyCatColumnName]]
    dfA['tech,cat']=list(zip(dfA.Technology, dfA.TechnologyCategory))
    dfA.drop(technologyColumnName,axis=1,inplace=True)
    dfA.drop(technologyCatColumnName,axis=1,inplace=True)
    dfA.reset_index(inplace=True)
    dfA.drop('index',axis=1,inplace=True)
    return dfA.drop_duplicates('tech,cat')




def getListOfTechnologies(df,employeeNumber,employeeNrColumnName,technologyColumnName,technologyCatColumnName):
    df = getListOfTechnologiesAndCats(df,employeeNumber,employeeNrColumnName,technologyColumnName,technologyCatColumnName)
    return list(set([item[0] for item in df['tech,cat'].values]))


def getUniqueValuesInColumn(df,columnName):
    return df[columnName].unique()


def getTechFromExperience():
    df = getExperienceTechDataSet()
    employeeNumbers = getUniqueValuesInColumn(df, 'employeeNumber')
    for item in employeeNumbers:
        print((item, getListOfTechnologies(df, item, 'employeeNumber', 'Technology', 'TechnologyCategory')))



getTechFromExperience()
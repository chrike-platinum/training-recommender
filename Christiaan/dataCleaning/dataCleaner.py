__author__ = 'christiaan'

from Christiaan import DataFrameLoader

def cleanTechWord(techWord):
    TechWordSplit = techWord.lower().replace('(',' ').replace(')',' ').replace('/',' ').split(' ')
    if TechWordSplit[0]=='microsoft' or TechWordSplit[0]=='ms':
        return TechWordSplit[1]+'(ms)'
    elif  TechWordSplit[0]=='bo':
        return 'sap'
    else:
        return TechWordSplit[0]

def cleanTechColumn(df,columnName):
     df[columnName]=list(map(lambda x: cleanTechWord(x),df[columnName]))
     return df


def getExperienceTechDataSet():
    df = DataFrameLoader.getTableauData('experiences+technology')
    print(list(df))
    df = df[['Employee Number','Name','Name (dim levelsofexperience.csv)','Name (dim technologycategories.csv)']]
    df.columns = ['employeeNumber','Technology','ExperienceLevel','TechnologyCategory']
    df = df.sort_values('employeeNumber')
    df = cleanTechColumn(df,'Technology')
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

df = getExperienceTechDataSet()
employeeNumbers = getUniqueValuesInColumn(df,'employeeNumber')
for item in employeeNumbers:
    print((item,getListOfTechnologies(df,item,'employeeNumber','Technology','TechnologyCategory')))

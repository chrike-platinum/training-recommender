__author__ = 'christiaan'

from Christiaan import DataFrameLoader

def cleanTechWord(techWord):
    TechWordSplit = techWord.lower().replace('.',' ').replace('(',' ').replace(')',' ').replace('/',' ').replace(':', ' ').split(' ')
    if TechWordSplit[0]=='microsoft' or TechWordSplit[0]=='ms':
        if len(TechWordSplit) > 1:
            if TechWordSplit[1]=='visual':
                return TechWordSplit[0]+' '+TechWordSplit[1]
            else:
                return TechWordSplit[1]#+' (ms)'
        else:
            return TechWordSplit[0]
    elif  TechWordSplit[0]=='bo' or TechWordSplit[0]=='business' and TechWordSplit[1]=='objects':
        return 'sap'#TechWordSplit[1]+' (sap)'
    elif  TechWordSplit[0]=='complete':
        return TechWordSplit[1]
    elif  TechWordSplit[0]=='visual':
        return TechWordSplit[0]+' '+TechWordSplit[1]
    elif  TechWordSplit[0]=='machine':
        return TechWordSplit[0]+' '+TechWordSplit[1]
    elif  TechWordSplit[0]=='big':
        return TechWordSplit[0]+' '+TechWordSplit[1]
    elif TechWordSplit[0]=='oracle':
        return 'oracle'#TechWordSplit[1]#+' (oracle)'
    elif TechWordSplit[0]=='open':
        return TechWordSplit[0]+' '+TechWordSplit[1]
    elif TechWordSplit[0]=='power':
        return TechWordSplit[0]+' '+TechWordSplit[1]
    elif TechWordSplit[0]=='business':
        return TechWordSplit[0]+' '+TechWordSplit[1]
    elif TechWordSplit[0]=='data':
        return TechWordSplit[0]+' '+TechWordSplit[1]
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


#getTechFromExperience()

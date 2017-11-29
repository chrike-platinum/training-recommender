__author__ = 'christiaan'

from Christiaan import DataFrameLoader

def cleanTechWord(techWord):
    TechWordSplit = techWord.lower().replace('.',' ').replace('(',' ').replace(')',' ').replace('/',' ').split(' ')
    if TechWordSplit[0]=='microsoft' or TechWordSplit[0]=='ms':
        if TechWordSplit[1]=='visual':
            return TechWordSplit[0]+' '+TechWordSplit[1]+' (ms)'
        else:
            return TechWordSplit[1]#+' (ms)'
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
    else:
        return TechWordSplit[0]

def cleanTechColumn(df,columnName):
     df[columnName]=list(map(lambda x: cleanTechWord(x),df[columnName]))
     return df

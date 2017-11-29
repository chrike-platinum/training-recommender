__author__ = 'christiaan'

import pandas as pd
from DataLoading.CSVLoader import load_CSVs



def join(dfs,primDf,secDf,key):
    suffix_X='_x'
    suffix_Y='_Y'
    if isinstance(primDf, str):
        suffix_X=str(primDf)
        primDf = dfs[primDf]
    if isinstance(secDf, str):
        suffix_Y=str(secDf)
        secDf = dfs[secDf]

    print('prim',primDf)
    print('sec',secDf)

    if isinstance(key, str):
        mergedDF = primDf.merge(secDf,how='left',on=key,suffixes=('_'+suffix_X, '_'+suffix_Y))
        assert(mergedDF.shape[1]==(primDf.shape[1]+secDf.shape[1]-1))
    else:
        mergedDF = primDf.merge(secDf,how='left',left_on=key[0],right_on=key[1],suffixes=('_'+suffix_X, '_'+suffix_Y))
        assert(mergedDF.shape[1]==(primDf.shape[1]+secDf.shape[1]))
    return mergedDF

def remove_key(df,key):
    return df.drop(key,axis=1,inplace=True)


#dfs = load_CSVs('/Users/christiaan/Desktop/2017/20171030_extract_erp_be/',3)

dfs = load_CSVs('/Users/christiaan/Desktop/2017/delimitersChanges/',3)


filenames = ['businessbackground.csv', 'dim_businesssector.csv', 'dim_department.csv',
 'dim_division.csv', 'dim_educationlevels.csv', 'dim_employeetypes.csv',
 'dim_levelsofexperience.csv', 'dim_profiles.csv', 'dim_technologycategories.csv',
 'dim_trainingfield.csv', 'education.csv', 'employeefield.csv', 'employees.csv',
 'employees_education.csv', 'employees_languages.csv', 'employees_levels.csv',
 'employees_profiles.csv', 'employees_skills.csv', 'employers.csv', 'entity.csv',
 'experiences.csv', 'practice.csv', 'roles.csv', 'technicalbackground.csv',
 'technology.csv', 'training.csv', 'traininginstitutions.csv', 'userallocation.csv',
 'users.csv']


'''
#dfs2 =[dfs['education.csv'],dfs['dim_educationlevels.csv']]
dfEdu = join(dfs,'education.csv','dim_educationlevels.csv','EducationLevel_ID')

dfEdu2 = join(dfs,dfEdu,key='Education_ID')
remove_key(df3,'EducationLevel_ID')
'''


def getEmployeeVSSkills():
    dfEmpl = join(dfs,'technology.csv','dim_technologycategories.csv','Category_ID')
    dfEmpl = join(dfs,'employees_skills.csv',dfEmpl,'Technology_ID')
    dfEmpl = join(dfs,'employees.csv',dfEmpl,'EmployeeNumber')
    #dfEmpl=join(dfs,dfEmpl,'mappingconsultantidemployeeid.csv',['Employee_ID','EmployeeNumber'])


    dfEmpl=join(dfs,dfEmpl,'technicalbackground.csv','Technology_ID')
    full = dfEmpl
    full.to_csv('result_full.csv')
    dfEmpl= dfEmpl[['EmployeeNumber','Employee_ID','Firstname','Lastname','FullTimePercentage','Skill_ID','BusinessSector_ID','Name_technology.csv',
          'Name_technology.csv','Description_technology.csv','Name_dim_technologycategories.csv','Description_dim_technologycategories.csv','LevelOfExperience_ID','Experience_ID']]
    dfEmpl=join(dfs,dfEmpl,'dim_levelsofexperience.csv','LevelOfExperience_ID')
    #dfEmpl.drop('EmployeeNumber',axis=1,inplace=True)
    return dfEmpl


def getTechBackgroundDF():
    print(dfs)
    dfEmpl = join(dfs,'employees.csv','experiences.csv','EmployeeNumber')
    return dfEmpl






#getTechBackgroundDF().to_csv('Businessunits.csv',sep='|')


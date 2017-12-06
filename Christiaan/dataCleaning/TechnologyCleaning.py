from Christiaan.csvLoading.CSVLoader import read_csv_tableau
from Christiaan.dataCleaning.dataCleaner import cleanTechColumn
import pandas as pd


def getTechListEmployees():
    filename = '/Users/christiaan/Desktop/tableau_technology_export.csv'
    df = read_csv_tableau(filename, filename)
    # df = df[['Employee Number','Firstname','Lastname','Level1','Practice1','Suggested Daily Rate','Name','Name (dim technologycategories.csv)']]
    df = df[['Employee Number', 'Firstname Firstname', 'Lastname Lastname', 'Level Level', 'Practice Practice',
             'Suggested Daily Rate', 'Name Name']]
    df.columns = ['Employee Number', 'Firstname', 'Lastname', 'Level', 'Practice', 'Suggested Daily Rate', 'Technology']
    df.sort_values('Employee Number', inplace=True)
    # df['Technology'] = df['Technology'].str.lower()
    # Filter by Department = BI and BD&A
    departments = ['BI', 'BD&A']
    df_dep = df[df['Practice'].isin(departments)]
    # a = [x for x in df_dep['Technology']]
    # Clean Technology column values and drop duplicates
    df_dep = cleanTechColumn(df_dep, 'Technology')
    df_dep.drop_duplicates(inplace=True)
    # Obtain list of Technologies for each employee
    emp_num = df_dep['Employee Number'].unique()
    emp_tech_list = [df_dep.loc[df_dep['Employee Number'] == num, 'Technology'].values.tolist() for num in emp_num]
    # Remove Technology column and unify rows for each employee
    df_dep = df_dep.drop('Technology', axis=1).drop_duplicates()
    # Convert df to list of lists (for each row)
    row_vals = df_dep.values.tolist()

    #'Geoffrey', 'Moerenhoudt'
    #'Vasilij', 'Nevlev'
    #'Faisal', 'Orakzai' -> senior
    #'Pieter', 'Vandamme' -> director

    row_vals = [employee if employee[1]!='Faisal' and employee[2]!='Orakzai' else [employee[0],employee[1],employee[2],'Senior',employee[4],employee[5]] for employee in row_vals]
    row_vals = [employee for employee in row_vals if employee[3]!='unknown' or employee[3]!='unknown']



    # Zip row values and Technologies
    emp_tech_tuples = [tuple((a) + [b]) for a, b in zip(row_vals, emp_tech_list)]
    return  emp_tech_tuples



print(getTechListEmployees())





#print(
#df_dep.loc[df_dep['Employee Number']==6,'Technology'])
#b = [x for x in df_dep['Technology']]

#ab = zip(a, b)
#[print(i) for i in ab]

#[print(i, j) for i, j in enumerate(df_dep['Technology'])]

#print(df_dep['Technology'])

#df_dep['Tech_Group'] = df_dep.Technology.str.split(' ', expand = True)[0].str.split('/', expand = True)[0]
#df_dep['Tech_Group'] = df_dep.Tech_Group.str.split('/', expand = True)[0]

# Split BI and BD&A Datasets
#df_bi = df_dep[df_dep['Practice'] == 'BI']
#df_bda = df_dep[df_dep['Practice'] == 'BD&A']

#print(df_bi.head())
#print(df_bda.head())

#print(df.info())
#print(df.head())
#print(df.describe())
#print(df_dep['Tech_Group'].value_counts(sort=True, dropna=False))

#print(df_bi['Technology'].value_counts(sort=True))
#print(df_bda['Technology'].value_counts(sort=True))

#print(df_dep['Technology'].str.split()[0])
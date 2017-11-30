from Christiaan.csvLoading.CSVLoader import read_csv_tableau
from Christiaan.dataCleaning.dataCleaner import cleanTechColumn
import pandas as pd

def readTechCSV(filename):
    df = read_csv_tableau(filename, filename)
    df = df[['Employee Number', 'Firstname Firstname', 'Lastname Lastname', 'Level Level', 'Practice Practice', 'Suggested Daily Rate', 'Name Name']]
    df.columns =['Employee Number', 'Firstname', 'Lastname', 'Level', 'Practice', 'Suggested Daily Rate', 'Technology']
    df.sort_values('Employee Number', inplace=True)
    return df

def cleanTech(dataFrame, techColumnName):
    df = cleanTechColumn(dataFrame, techColumnName)
    df.drop_duplicates(inplace=True)
    return df

# Read Tableau csv export
file = 'tableau_technology_export.csv'
df = readTechCSV(file)

# Filter by Department = BI and BD&A
departments = ['BI', 'BD&A']
df_dep = df[df['Practice'].isin(departments)]

# Clean Technology column values and drop duplicates
df_dep = cleanTech(df_dep, 'Technology')

# Obtain list of Technologies for each employee
emp_num = df_dep['Employee Number'].unique()
emp_tech_list = [df_dep.loc[df_dep['Employee Number']==num, 'Technology'].values.tolist() for num in emp_num]

# Remove Technology column and unify rows for each employee
df_dep = df_dep.drop('Technology', axis=1).drop_duplicates()

# Convert df to list of lists (for each row)
row_vals = df_dep.values.tolist()

# Zip row values and Technologies
emp_tech_tuples = [tuple([*row_vals[i], emp_tech_list[i]]) for i in range(len(emp_tech_list))]

#print(emp_tech_tuples)




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
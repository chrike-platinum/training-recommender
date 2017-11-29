from Christiaan.CSVLoader import read_csv_tableau
from Christiaan.dataCleaning.dataCleaner import cleanTechColumn
import pandas as pd
import os

os.chdir(r'C:\Users\adebola.oshomoji\Documents\KEYRUS_Bootcamp_November\2017')

filename = 'tableau_technology_export.csv'
df = read_csv_tableau(filename, filename)

#df = df[['Employee Number','Firstname','Lastname','Level1','Practice1','Suggested Daily Rate','Name','Name (dim technologycategories.csv)']]
df = df[['Employee Number', 'Firstname Firstname', 'Lastname Lastname', 'Level Level', 'Practice Practice', 'Suggested Daily Rate', 'Name Name', 'Name Name (dim_technologycategories.csv)']]
df.columns =['Employee Number', 'Firstname', 'Lastname', 'Level', 'Practice', 'Suggested Daily Rate', 'Technology', 'Technology Category']
df.sort_values('Employee Number', inplace=True)

#df['Technology'] = df['Technology'].str.lower()

# Filter by Department = BI and BD&A
departments = ['BI', 'BD&A']
df_dep = df[df['Practice'].isin(departments)]

test = cleanTechColumn(df_dep, 'Technology')

print(test.Technology)

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
__author__ = 'christiaan'
import pandas as pd
import numpy as np

from Christiaan.csvLoading.CSVLoader import read_csv

def initializeData():
    df = pd.read_csv('training.csv',encoding='utf-16',sep='|',decimal=',')
    df = df[['TrainingName','TotalCost']]
    df['TrainingName']=df['TrainingName'].str.lower()
    #df['TotalCost']=df['TotalCost'].apply(lambda x: x.str.replace(",","."))
    df.to_csv('trainingCosts.csv',sep='|')

def calculateCost(tech,df):
    if len(tech)>=3:
        returndf = df[[tech in item.lower() for item in df['TrainingName']]]
    elif len(tech)==1:
        returndf = df[[' '+tech+' ' in item.lower() for item in df['TrainingName']]]
    elif len(tech)>=2:
        returndf = df[[tech+' ' in item.lower() for item in df['TrainingName']]]
    mean = round(returndf['TotalCost'].mean(),0)
    if np.isnan(mean):
        print("training cost for "+str(tech)+" is an estimation (median of all trainings)!")
        mean = df['TotalCost'].median()
    return mean


'''
df=pd.read_csv('trainingCosts.csv',sep='|')
print(calculateCost('latex',df))
'''
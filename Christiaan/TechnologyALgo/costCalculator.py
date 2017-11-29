__author__ = 'christiaan'



from Christiaan.csvLoading.CSVLoader import read_csv

def initializeData():
    df = read_csv('training.csv','training.csv')
    df = df[['TrainingName','TotalCost']]
    df['TrainingName']=df['TrainingName'].str.lower()
    df['TotalCost']=df['TotalCost'].apply(lambda x: x.str.replace(",","."))
    df.to_csv('trainingCosts.csv',sep='|')


initializeData()

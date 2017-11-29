__author__ = 'christiaan'

import pandas as pd
import os
from multiprocessing import Pool
from chardet.universaldetector import UniversalDetector
import chardet
import glob
import csv
from io import StringIO

'''
def read_csv(filename):
    'converts a filename to a pandas dataframe'
    print('filename',filename)
    rawdata = pd.read_csv(filename)
    print(chardet.detect(rawdata))
    file = pd.read_csv(filename,encoding='utf-16_le',error_bad_lines=False)
    return file
'''

def read_csv(filename,simplefileName):
    '''converts a filename to a pandas dataframe
    TODO: Fix complete ExceptionHandlers'''
    print('reading: '+str(simplefileName))
    try:
        detector = UniversalDetector()
        for fname in glob.glob(filename):
            detector.reset()
            for line in open(fname, 'rb'):
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
        print('Encoding detected: '+str(detector.result['encoding'])+' with confidence: '+str(detector.result['confidence'])*100+'%')
        return pd.read_csv(filename,delimiter='|',encoding=detector.result['encoding'])

    except:
        return pd.read_csv(filename,delimiter='|',encoding=detector.result['encoding'], error_bad_lines=False)



def read_csv_tableau(filename,simplefileName):
    '''converts a filename to a pandas dataframe
    TODO: Fix complete ExceptionHandlers'''
    print('reading: '+str(simplefileName))
    try:
        detector = UniversalDetector()
        for fname in glob.glob(filename):
            detector.reset()
            for line in open(fname, 'rb'):
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
        print('Encoding detected: '+str(detector.result['encoding'])+' with confidence: '+str(detector.result['confidence'])*100+'%')
        return pd.read_csv(filename,delimiter='\t',encoding=detector.result['encoding'])

    except:
        return pd.read_csv(filename,delimiter='\t',encoding=detector.result['encoding'], error_bad_lines=False)


def load_CSVs(dir,numberOfPools):
    #pool = Pool(processes=numberOfPools) # or whatever your hardware can support
    file_list,file_names = get_file_names(dir)
    df_list = {name:read_csv(file,name) for file,name in zip(file_list,file_names)}
    #df_list = pool.map(read_csv, file_list)
    return df_list


def get_file_names(dir):
    files = os.listdir(dir)
    extended_file_name_list = [dir + filename for filename in files if filename.split('.')[1] == 'csv']
    simple_file_name_list = [filename for filename in files if filename.split('.')[1] == 'csv']
    return extended_file_name_list,simple_file_name_list



def replaceDelimiters(dir):
    dfs = load_CSVs(dir,3)
    for key, value in dfs.items():
        print(value)
        value.to_csv(key,sep='|') #Alter delimiter reading above!



#print('start')
#df = read_csv_tableau('/Users/christiaan/Desktop/employees+levels+technologies.csv','employees+levels+technologies.csv')
#print(list(df))
#df=df[['Employee Number','Firstname','Lastname','Level1','Practice1','Suggested Daily Rate','Name','Name (dim technologycategories.csv)']]
#df=df.sort_values('Employee Number')
#df.to_csv('employeeData.csv',index=False)

#replaceDelimiters('/Users/christiaan/Desktop/2017/new data/')

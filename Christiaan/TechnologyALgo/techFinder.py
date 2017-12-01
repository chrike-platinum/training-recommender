__author__ = 'christiaan'

import numpy as np
import pandas as pd
import pulp
from Christiaan.TechnologyALgo.employeeTransformer import getTechList
from Christiaan.TechnologyALgo.employeeTransformer import getAllUpdatedEmployeeData
from Christiaan.ClusterMaker.cluster import calculateMostSimilarExperts
from Christiaan.TechnologyALgo.costCalculator import calculateCost
dfCost=pd.read_csv('trainingCosts.csv',sep='|')

def initializeData():
    #employees = getAllUpdatedEmployeeData(['BI','BD&A'])
    BIregulars,BDAregulars = calculateMostSimilarExperts()
    BItech=getTechList('BI',50)
    BDAtech=getTechList('BD&A',50)

    #BIregulars2=[BIemployee.setlistOfPossibleTechs(BItech) for BIemployee in BIregulars]
    BDAregulars2=[BDAemployee.setlistOfPossibleTechs(BDAtech) for BDAemployee in BDAregulars]

    #BIregulars3=[BIemployee.updateVerboseTechList(dfCost) for BIemployee in BIregulars2]
    BDAregulars3=[BDAemployee.updateVerboseTechList(dfCost) for BDAemployee in BDAregulars2]
    return BDAregulars3


def initializeProblem(employee):
    sortedList = sorted(employee.verboseTechList,key=lambda x: x[0])
    expertList = employee.mostSimilarExpert.getTechList()
    ownList = employee.getTechList()

    techs = [item[0] for item in sortedList]
    ExpertRecommendedList = [1 if tech in expertList else 0 for tech in techs]
    AlreadySatisfiedTechs = [1 if tech in ownList else 0 for tech in techs]
    weights = [item[1] for item in sortedList]
    costs = [item[2] for item in sortedList]
    technologies = np.matrix([weights,costs,ExpertRecommendedList,AlreadySatisfiedTechs]).T
    namesdf = techs
    df = pd.DataFrame(technologies,columns=['Weights','Cost','ExpertRecommended','AlreadyKnown'],index=namesdf)
    #print('employeeList',employee.getTechList())
    #print('ExpertList',employee.mostSimilarExpert.getTechList())
    return df

def createConstraintProgrammingModel(df,numberOfExpertTech,numberOfRandomTech):
    names = pulp.LpVariable.dicts("var", df.index, lowBound=0,upBound=1, cat='Integer')
    model = pulp.LpProblem("find optimal set of Technologies to train", pulp.LpMaximize)
    #optimize weights
    model += sum([df.loc[i].values[0] * names[i] for i in df.index])

    #cost may not be higher than 8500
    model += sum([names[idx]*df.loc[idx].values[1]  for idx in df.index]) <= 8500

    #Skill can not already be known by the employee
    model += sum([names[idx]*df.loc[idx].values[3]  for idx in df.index]) == 0

    #number of expert tech choosings must be equal or lower than...
    model += sum([names[idx]*df.loc[idx].values[2]  for idx in df.index]) == numberOfExpertTech

    #number of Random tech choosings must be equal or lower than...
    model += sum([names[idx]*(1-df.loc[idx].values[2])  for idx in df.index]) == numberOfRandomTech


    model.solve()
    solution = [idx for idx in df.index if names[idx].value()==1]
    expectedCost = sum([calculateCost(tech,dfCost) for tech in solution])


    print(solution,expectedCost)

    return model

def getTechRecommendations():
    BDAregulars3 = initializeData()

    '''
    for employee in BDAregulars3:
        df = initializeProblem(employee)
        createConstraintProgrammingModel(df,5,3)
    '''
    return BDAregulars3

    '''
    for employee in BIregulars3:
        df = initializeProblem(employee)
        createConstraintProgrammingModel(df,5,3)

    '''








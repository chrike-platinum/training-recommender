__author__ = 'christiaan'

import numpy as np
import pandas as pd
import pulp


from Christiaan.Engines.CostEngine import calculateCost




def initializeProblem(employee):
    '''
    Initialize a dataframe which is used for the linear programming
    This dataframe has as index the name of a technology
    The columns: market importance, estimated training cost, mentor recommended (1 or 0), tech already known by employee (1 or 0)
    :param employee: employee to build a model for
    :return:
    '''
    sortedList = sorted(employee.listOfTechObjectsToSuggest,key=lambda x: x.getName())
    expertList = [tech.getName() for tech in employee.mostSimilarMentor.getPossessedTechSkills()]
    ownList = [tech.getName() for tech in employee.getPossessedTechSkills()]


    techs = [tech.getName() for tech in sortedList]
    ExpertRecommendedList = [1 if tech in expertList else 0 for tech in techs]
    AlreadySatisfiedTechs = [1 if tech in ownList else 0 for tech in techs]
    weights = [tech.getMarketImportance() for tech in sortedList]
    costs = [tech.getEstimatedTrainingCost() for tech in sortedList]
    technologies = np.matrix([weights,costs,ExpertRecommendedList,AlreadySatisfiedTechs]).T
    namesdf = techs
    df = pd.DataFrame(technologies,columns=['marketImportance','Cost','mentorRecommended','AlreadyKnown'],index=namesdf)
    return df



def createLinearProgrammingModel(df,numberOfMentorTech,numberOfRandomTech,employee):
    '''
    Construct the linear programming model
    :param df: input df
    :param numberOfMentorTech: number of technologies suggested by the mentor
    :param numberOfRandomTech: number of technologies suggested by the market
    :param employee: trainee to recommend trainings for
    :return:
    '''

    names = pulp.LpVariable.dicts("var", df.index, lowBound=0,upBound=1, cat='Integer')
    model = pulp.LpProblem("Find optimal set of Technologies to train", pulp.LpMaximize)
    #optimize weights
    model += sum([df.loc[i].values[0] * names[i] for i in df.index])

    #cost may not be higher than 8500
    model += sum([names[idx]*df.loc[idx].values[1]  for idx in df.index]) <= 8500

    #Skill can not already be known by the employee
    model += sum([names[idx]*df.loc[idx].values[3]  for idx in df.index]) == 0

    #number of expert tech choosings must be equal or lower than...
    model += sum([names[idx]*df.loc[idx].values[2]  for idx in df.index]) == numberOfMentorTech

    #number of Random tech choosings must be equal or lower than...
    model += sum([names[idx]*(1-df.loc[idx].values[2])  for idx in df.index]) == numberOfRandomTech


    model.solve()
    solution = [(idx,df.loc[[idx]]['Cost'].values[0],df.loc[[idx]]['marketImportance'].values[0],employee.isInMentorList(idx)) for idx in df.index if names[idx].value()==1]
    EstTotalCost = sum([tech[1] for tech in solution])

    return solution, EstTotalCost










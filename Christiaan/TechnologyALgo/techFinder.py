__author__ = 'christiaan'

import numpy as np
import pandas as pd
import pulp

def initializeProblem():
    technologies = np.matrix([[0.5,0.1,0.9,0.01],[1,1,1,1]]).T
    namesdf = ['tech1','tech2','tech3','tech4']
    df = pd.DataFrame(technologies,columns=['weight','pref'],index=namesdf)
    return df

def createConstraintProgrammingModel(df):
    names = pulp.LpVariable.dicts("var", df.index, lowBound=0,upBound=1, cat='Integer')
    model = pulp.LpProblem("find optimal set of Technologies to train on", pulp.LpMaximize)
    model += sum([df.loc[i].values[0] * names[i] + df.loc[i].values[1] * names[i] for i in df.index])


    model += sum([names[idx] for idx in df.index]) <= 2



    model.solve()
    for idx in df.index:
        print(idx, names[idx].value())
    return model

df = initializeProblem()
createConstraintProgrammingModel(df)

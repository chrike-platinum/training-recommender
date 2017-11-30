__author__ = 'christiaan'


from scipy.spatial import distance
from Christiaan.dataCleaning.TechnologyCleaning import getTechListEmployees
from Christiaan.TechnologyALgo import employeeTransformer

def calculateSimilarity(Xa,Xb):
    return distance.euclidean(Xa,Xb)

#expertsDFTuples: list of tuples containing employeeID expect and feature vector expert
#junior: tuple of employee id and feature vector junior
def getMostSimilarExpert(experts,employee):
    similarityList =[]
    for expert in experts:
        similarityList.append((expert,calculateSimilarity(expert.getFeatureVector(),employee.getFeatureVector())))
    return max(similarityList,key=lambda item:item[1])[0]

def getExpertsList(practice):
    employees = employeeTransformer.getAllUpdatedEmployeeData(['BI','BD&A'],40)
    return [employee for employee in employees if employee.hasExpertStatus()==True and employee.practice==practice]

def getRegularsList(practice):
    employees = employeeTransformer.getAllUpdatedEmployeeData(['BI','BD&A'],40)
    return [employee for employee in employees if employee.hasExpertStatus()==False and employee.practice==practice]


def calculateMostSimilarExperts():
    expertsBI = getExpertsList('BI')
    regularsBI= getRegularsList('BI')
    BIregulars = [employee.setMostSimilarExpert(getMostSimilarExpert(expertsBI,employee))for employee in regularsBI]

    expertsBDA = getExpertsList('BD&A')
    regularsBDA= getRegularsList('BD&A')
    BDAregulars=[employee.setMostSimilarExpert(getMostSimilarExpert(expertsBDA,employee))for employee in regularsBDA]

    return BIregulars,BDAregulars



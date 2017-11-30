__author__ = 'christiaan'

from Christiaan.dataCleaning.TechnologyCleaning import getTechListEmployees
from Christiaan.dataObjects.employee import EmployeeObject
from collections import Counter
import operator
from numpy import random

def getFeatureVector(employeeList,practice,N):
    employeesExpertsSkills = [item.getTechList() for item in employeeList if item.hasExpertStatus() and item.getPractice()==practice]
    employeesExpertsSkills = [item for sublist in employeesExpertsSkills for item in sublist]
    employeesExpertsSkillsCounter = Counter(employeesExpertsSkills)
    sorted_x = sorted(employeesExpertsSkillsCounter.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    return [item[0] for item in sorted_x[:N]]

def getEmployeeObjects():
    emplList = getTechListEmployees()
    employeeList = [EmployeeObject(item[0],item[1],item[2],item[3],item[4],item[5],item[6]) for item in emplList]
    return employeeList

def getAllUpdatedEmployeeData(practices,N):
    employeeList=getEmployeeObjects()
    featureVector1 = getFeatureVector(employeeList,practices[0],N)
    employeeList2 = [employee.setFeatureVector(featureVector1) if employee.getPractice()==practices[0] else employee for employee in employeeList]

    featureVector2 = getFeatureVector(employeeList,practices[1],N)
    employeeList3 = [employee.setFeatureVector(featureVector2) if employee.getPractice()==practices[1] else employee for employee in employeeList2]

    return employeeList3



def getTechList(practice,N):
    listOfTech = [employee.getTechList() for employee in getEmployeeObjects() if employee.getPractice()==practice]
    listOfTech = list(set([item for sublist in listOfTech for item in sublist]))


    random.seed(4)
    random.shuffle(listOfTech)


    listOfTech.remove('')
    return listOfTech


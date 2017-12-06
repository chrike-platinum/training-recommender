__author__ = 'christiaan'

from Christiaan.Engines.EmployeeFactory import getTechList
from Christiaan.Engines.EmployeeFactory import getAllUpdatedEmployeeData
from Christiaan.Engines.MentorEngine import setMostSimilarMentor
from Christiaan.Engines import LinProgEngine
import pandas as pd

dfCost=pd.read_csv('trainingCosts.csv',sep='|')

def initializeData(practices):
    '''
    Initialize the employee objects used for the optimization:
    -get all employee objects per practice
    -pair them with the most similar mentor
    -populate them with a list of all possible tech
    :return: dictionary of employees per practice, split in mentors and trainees
    '''
    employees=[]
    for practice in practices:
        employees.append(getAllUpdatedEmployeeData(practice,40))
    employees = [employee for sublist in employees for employee in sublist]
    employeesPerPractice = setMostSimilarMentor(employees,practices)
    for practice in employeesPerPractice:
        numberOfTech=50
        tech=getTechList(employees,practice,numberOfTech)
        for employee in employeesPerPractice[practice]['trainees']:
            employee.setlistOfTechNamesToSuggest(tech)
            #employee.updateListOfTechObjectsToSuggest(dfCost) #eager data collection


    return employeesPerPractice


def getAllTrainees(practices):
    '''
    Returns all the trainee objects
    :param practices: businessunit
    :return: list of trainee objects
    '''
    practiceDistri = initializeData(practices)
    trainees=[]
    for practice in practiceDistri:
        trainees.append(practiceDistri.get(practice).get('trainees'))
    listOfTrainees = [trainee for traineeListPerPractice in trainees for trainee in traineeListPerPractice]
    return listOfTrainees


def getAllEmployeesDictionary(practices):
    '''
    Returns a dictionary of all the employee objects
    :param practices: business unit
    :return: dictionary of employees split on practices and trainee vs mentors
    '''
    return initializeData(practices)

def getRecommendedTrainingsForEmployee(employee,numberOfMentorCourses,numberOfExtraCourses):

    employee.setmarketImportanceCalculator()

    employee.getUpdatedListOfTechObjectsToSuggest(dfCost) #update cost and market importance
    df = LinProgEngine.initializeProblem(employee)
    solution,estTotalCost=LinProgEngine.createLinearProgrammingModel(df,numberOfMentorCourses,numberOfExtraCourses,employee)
    return solution,estTotalCost
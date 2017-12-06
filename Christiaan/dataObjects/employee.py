__author__ = 'christiaan'
from Christiaan.Engines.MarketTrendsEngine import getMarketImportanceOfTech
from Christiaan.Engines.CostEngine import calculateCost
from Christiaan.dataObjects.TechnologySkill import TechnologySkill


class Employee(object):
    def __init__(self,employeeID,fName,lName,title,practice,suggestedCost,possessedTechSkills):
        '''
        Represents a employee object
        :param employeeID:
        :param fName:
        :param lName:
        :param title:
        :param practice:
        :param suggestedCost:
        :param possessedTechSkills:
        :return: None
        '''
        self.fName = fName
        self.lName = lName
        self.employeeID = employeeID
        self.title= title
        self.practice= practice
        self.suggestedCost= suggestedCost
        self.possessedTechSkills=possessedTechSkills
        self.skillFeatureVector=[]
        self.mostSimilarMentor=None
        self.listOfTechNamesToSuggest=[]
        self.listOfTechObjectsToSuggest=[]
        self.costCalculatorFunction=None
        self.marketTrendCalculatorFunction=None


    def getFname(self):
        '''
        :return: the first name of the employee
        '''
        return self.fName

    #returns the last name of the employee
    def getLname(self):
        return self.lName

    #returns the ID of the employee
    def getEmployeeID(self):
        return self.employeeID

    #returns the title of the employee
    def getTitle(self):
        return self.title

    #returns the practice of the employee
    def getPractice(self):
        return self.practice

    #returns the suggested cost of the employee
    def getSuggestCost(self):
        return self.suggestedCost

    #returns the list of tech skills that the employee posseses
    def getPossessedTechSkills(self):
        return self.possessedTechSkills

    #returns the featurevector to calculate the similarity to other employees
    def getSkillFeatureVector(self):
        return self.skillFeatureVector

    #sets the list of possible techs that are presented to the employee to learn about
    def setlistOfTechNamesToSuggest(self,generalTechList):
        expertList = [tech.name for tech in self.mostSimilarMentor.getPossessedTechSkills()]
        listPosTech = list(set().union(expertList,generalTechList))
        self.listOfTechNamesToSuggest=listPosTech


    #normalizes the market impotance between (0 and 1) of all the tech skills that are presented to the employee
    def normalizeMarketImportance(self):
        weightList = [techSKill.getMarketImportance() for techSKill in self.listOfTechObjectsToSuggest]
        minW = min(weightList)
        maxW = max(weightList)
        for tech in self.listOfTechObjectsToSuggest:
            tech.setMarketImportance((tech.getMarketImportance()-minW)/(maxW-minW))


    #makes list of objects of the suggested tech names, marketImportance and estimated cost
    def updateListOfTechObjectsToSuggest(self,dfCost):
        self.listOfTechObjectsToSuggest = [TechnologySkill(tech,getMarketImportanceOfTech(tech),calculateCost(tech,dfCost)) for tech in self.listOfTechNamesToSuggest]
        self.normalizeMarketImportance()


    def getUpdatedListOfTechObjectsToSuggest(self,dfCost):
        self.updateListOfTechObjectsToSuggest(dfCost)
        return self.listOfTechObjectsToSuggest


#   #sets the feature vector of the employee (1 of has skill, 0 if not)
    def setSkillFeatureVector(self,featureVector):
        self.skillFeatureVector= [1 if item in self.getPossessedTechSkills() else 0 for item in featureVector]


    #sets the most similar mentor to the employee
    def setMostSimilarExpert(self,Expert):
        self.mostSimilarMentor=Expert
        return self

    #Boolean: 1=mentor, 0=trainee
    def isMentor(self):
        if len(self.getTitle().split(' '))==1:
            return self.getTitle().split(' ')[0].lower()=='senior' or self.getTitle().split(' ')[0].lower()=='expert' or self.getTitle().split(' ')[0].lower()=='manager'
        else:
            return self.getTitle().split(' ')[0].lower()=='senior' and self.getTitle().split(' ')[1].lower()!='manager' or self.getTitle().split(' ')[0].lower()=='expert'

    def isInMentorList(self,tech):
        '''
        boolean wether a tech skill is in the mentor list or not
        :param tech: tech skill
        :return: True if tech skill is in list of mentor, False if not
        '''
        return tech in [skill.getName() for skill in self.mostSimilarMentor.getPossessedTechSkills()]


    #Returns a string representation of the employee object
    def __str__(self):
        if self.mostSimilarMentor==None:
            return '--------\n'+str(self.employeeID) +'\n'+ str(self.fName) +'\n'+ str(self.lName) +'\n'+ str(self.title) +'\n' \
                            + str(self.practice)+'\n'+ str(self.possessedTechSkills)+'\n'+ str(self.skillFeatureVector)+'\n'+ str(self.mostSimilarMentor)
        else:

            return '--------\n'+str(self.employeeID) +'\n'+ str(self.fName) +'\n'+ str(self.lName) +'\n'+ str(self.title) +'\n' \
                            + str(self.practice)+'\n'+ str(self.possessedTechSkills)+'\n'+ str(self.skillFeatureVector)+'\n'+ str(self.mostSimilarMentor.fName)




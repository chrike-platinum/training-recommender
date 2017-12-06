__author__ = 'christiaan'

#represents a technology skill object
class TechnologySkill(object):


    #constructor
    def __init__(self,name,marketImportance,estimatedTrainingCost,proficiency=None):
        self.name = name
        self.marketImportance = marketImportance
        self.estimatedTrainingCost = estimatedTrainingCost
        self.proficiency=proficiency


    #returns the technology name
    def getName(self):
        return self.name

    #returns the market importance
    def getMarketImportance(self):
        return self.marketImportance

    def setMarketImportance(self,newMarketImportance):
        self.marketImportance = newMarketImportance

    #returns the training cost
    def getEstimatedTrainingCost(self):
        return self.estimatedTrainingCost

    #returns the newest market importance (request newest market importance)
    def getNewestMarketImportance(self):
        #todo update here the market importance?
        return None

    #returns the user proficiency in this technology skill
    def getProficiency(self):
        return self.proficiency

    def setProficiency(self,proficiencyLevel):
        self.proficiency = proficiencyLevel
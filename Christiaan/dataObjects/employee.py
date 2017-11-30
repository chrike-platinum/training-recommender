__author__ = 'christiaan'
from Ade.Technology import getTechWeight

class EmployeeObject(object):
    def __init__(self,employeeID,Fname,Lname,Title,practice,suggestedCost,techList):
        self.Fname = Fname
        self.Lname = Lname
        self.employeeID = employeeID
        self.title= Title
        self.practice= practice
        self.suggestedCost= suggestedCost
        self.techList=techList
        self.featureVector=[]
        self.mostSimilarExpert=None
        self.listOfPossibleTechs=[]
        self.listSuggestedTechs=[]
        self.verboseTechList=[]

    def getFname(self):
        return self.Fname

    def getLname(self):
        return self.Lname

    def getEmployeeID(self):
        return self.employeeID

    def getTitle(self):
        return self.title

    def getPractice(self):
        return self.practice

    def getSuggestCost(self):
        return self.suggestedCost

    def getTechList(self):
        return self.techList

    def getFeatureVector(self):
        return self.featureVector

    def setlistOfPossibleTechs(self,generalTechList):
        expertList = self.mostSimilarExpert.getTechList() #todo delete from expertlist after
        self.listOfPossibleTechs=list(set().union(expertList,generalTechList))
        return self

    def updateVerboseTechList(self):
        self.verboseTechList = [(tech,getTechWeight(tech))for tech in self.listOfPossibleTechs]#todo add cost

    def setFeatureVector(self,featureVector):
        self.featureVector=[1 if item in self.getTechList() else 0 for item in featureVector]
        return self


    def setMostSimilarExpert(self,Expert):
        self.mostSimilarExpert=Expert
        return self

    def hasExpertStatus(self):
        if len(self.getTitle().split(' '))==1:
            return self.getTitle().split(' ')[0].lower()=='senior' or self.getTitle().split(' ')[0].lower()=='expert' or self.getTitle().split(' ')[0].lower()=='manager'
        else:
            return self.getTitle().split(' ')[0].lower()=='senior' and self.getTitle().split(' ')[1].lower()!='manager' or self.getTitle().split(' ')[0].lower()=='expert'

    def __str__(self):
        if self.mostSimilarExpert==None:
            return '--------\n'+str(self.employeeID) +'\n'+ str(self.Fname) +'\n'+ str(self.Lname) +'\n'+ str(self.title) +'\n' \
                            + str(self.practice)+'\n'+ str(self.techList)+'\n'+ str(self.featureVector)+'\n'+ str(self.mostSimilarExpert)
        else:

            return '--------\n'+str(self.employeeID) +'\n'+ str(self.Fname) +'\n'+ str(self.Lname) +'\n'+ str(self.title) +'\n' \
                            + str(self.practice)+'\n'+ str(self.techList)+'\n'+ str(self.featureVector)+'\n'+ str(self.mostSimilarExpert.Fname)


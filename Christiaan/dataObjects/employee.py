__author__ = 'christiaan'
from Ade.Technology import getTechWeight
from Christiaan.TechnologyALgo.costCalculator import calculateCost

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
        expertList = self.mostSimilarExpert.getTechList()

        listPosTech = list(set().union(expertList,generalTechList))
        #if '' in listPosTech:
        #    listPosTech.remove('')
        #    print('DETECTED-------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        self.listOfPossibleTechs=listPosTech
        return self

    def normalizeWeights(self):
        weightList = [item[1] for item in self.verboseTechList]
        minW = min(weightList)
        maxW = max(weightList)
        return [(weight-minW)/(maxW-minW) for weight in weightList]


    def updateVerboseTechList(self,dfCost):
        self.verboseTechList = [(tech,getTechWeight(tech),calculateCost(tech,dfCost))for tech in self.listOfPossibleTechs]#todo add cost
        normalizedWeightList = self.normalizeWeights()
        self.verboseTechList = [(item[0],normalizedWeight,item[2]) for item,normalizedWeight in zip(self.verboseTechList,normalizedWeightList)]
        return self


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


__author__ = 'christiaan'


from scipy.spatial import distance
from Christiaan.dataCleaning.TechnologyCleaning import getTechListEmployees
from Christiaan.Engines import EmployeeFactory

def calculateSimilarity(Xa,Xb):
    return distance.euclidean(Xa,Xb)

def calculateMostSimilarExpert(experts,employee):
    similarityList =[]
    for expert in experts:
        similarityList.append((expert,calculateSimilarity(expert.getSkillFeatureVector(),employee.getSkillFeatureVector())))
    return max(similarityList,key=lambda item:item[1])[0]

def getMentorList(employees,practice):
    return [employee for employee in employees if employee.isMentor()==True and employee.practice==practice]

def getTraineeList(employees,practice):
    return [employee for employee in employees if employee.isMentor()==False and employee.practice==practice]


def setMostSimilarMentor(employees,practices):
    mentorVSTraineeDistri={}
    for practice in practices:
        mentors = getMentorList(employees,practice)
        trainees = getTraineeList(employees,practice)
        mentorVSTraineeDistri.update({practice:{'mentors':mentors,'trainees':trainees}})

    for practice in mentorVSTraineeDistri:
        employees = mentorVSTraineeDistri[practice]['trainees']
        mentors = mentorVSTraineeDistri[practice]['mentors']
        for employee in employees:
            employee.setMostSimilarExpert(calculateMostSimilarExpert(mentors,employee))
    return mentorVSTraineeDistri


__author__ = 'christiaan'


from scipy.spatial.distance import cdist


def calculateSimilarity(Xa,Xb,metric='euclidean'):
    return cdist(Xa, Xb, metric=metric)


#expertsDFTuples: list of tuples containing employeeID expect and feature vector expert
#junior: tuple of employee id and feature vector junior

def getMostSimilarExpert(expertsDFTuples,junior):
    similarityList =[]
    for i in range(len(expertsDFTuples)):
        similarityList.append(expertsDFTuples[i][0],calculateSimilarity(expertsDFTuples[i][1],junior[1]))
        return max(similarityList,key=lambda item:item[1])[0]




import random
import gensim

DEFAULT_THRESHOLD = 0.6

#loading model
model = gensim.models.Word2Vec.load("word2vec.model")

def strsEval(a, b):
    return model.wv.similarity(w1=a,w2=b)

def shortAnswerMark(studAns, ansKey, threshold=DEFAULT_THRESHOLD, markForEmpty=0.0): #0 for threshold if no threshold
    if (studAns.isspace()):
        return markForEmpty
    studList = studAns.split(" ")
    keyList = ansKey.split(" ")

    totalScore = 0
    for i in range(0, len(studList)):
        curMaxScore = 0
        for j in range(0, len(keyList)):
            curScore = strsEval(studList[i], keyList[j])
            if (curScore > curMaxScore):
                curMaxScore = curScore
        totalScore += curMaxScore
    
    totalScore /= len(studList)
    mark = 0.0
    if (totalScore > threshold):
        mark = 1.0
        
    return mark

def multChoiceMark(studAns, ansKey, markForEmpty=0.0):
    if (studAns.isspace()):
        return markForEmpty
    
    if (studAns == ansKey):
        return 1.0
    else:
        return 0.0

if __name__ == "__main__":
    pass
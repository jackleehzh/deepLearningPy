import numpy as np
import Evaluation as elv
import EvaluateStandard as es
import random

def generateData(upperBound, row, col):
    return np.mat(np.random.randint(upperBound, size=(row, col)))

def divideLabel(data, col):
    index = col - 1
    dx = data[:,0:index]
    dy = data[:,index]
    return dx, dy

#线性回归，通过减少均方误差来优化参数
def linearRegression(trdx, trdy):
    return (trdx.T * trdx).I * trdx.T * trdy

def pridect(tsdx, w):
    return tsdx * w

def studyMachine(data, elvFunc, frequency):
    w = 0
    for i in range(frequency):
        tsdata, trdata = elv.divideData(data, elvFunc, i)
        trdx, trdy = divideLabel(trdata, 6)
        tsdx, tsdy = divideLabel(tsdata, 6)
        #printData(data, trdata, tsdata)
        w = w + linearRegression(trdx, trdy)
    w = w / frequency
    result = pridect(tsdx, w)
    return es.precisionRecall(result, tsdy, 0.49, 1)

def printData(data, trdata, tsdata):
    print("initial set")
    print(data)
    print("training set")
    print(trdata)
    print("testing set")
    print(tsdata)

def printResult(ret, tsdy):
    for i in range(len(ret)):
        print(ret[i], tsdy[i])

data = generateData(2, 100, 6)

result1 = studyMachine(data, elv.holdOut, 10)
result2 = studyMachine(data, elv.crossValidation, 10)
result3 = studyMachine(data, elv.bootStrapping, 10)
#printResult(ret, tsdy)

print(result1, result2, result3)

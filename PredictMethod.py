# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'

import graphlab
import matplotlib.pyplot as plt
import networkx as nx
from numpy import *
def loadDataSet(temp):
    dataMat = [[float(1),float(0)],[float(1),float(1)],[float(1),float(2)],[float(1),float(3)],[float(1),float(4)]]
    labelMat = [float(temp[0]),float(temp[1]),float(temp[2]),float(temp[3]),float(temp[4])]
    return dataMat,labelMat

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws*((0.8-testPoint[1]*0.016))
output=open('F:/github/WoLongBigData/DataManager/FirstResult.csv','w+')
with open('F:/github/WoLongBigData/DataManager/3000DepthAndWidth.txt','r') as f:
    for position, line in enumerate(f):
        print 1
        t= line.strip().split('\t')
        temp = t[1:6]
        width=[]
        depth=float(t[-1])+1.0
        xArr,yArr = loadDataSet(temp)
        for i in range(5,25):
            width.append(lwlr([1,float(i)],xArr,yArr,k=1).getA1()[0])
        for i in range(25,293):
            width.append(width[19])
        s=t[0]
        for i in width:
            s = s+','+str(i)
        for i in range(288):
            s = s+','+str(depth)
        output.writelines(s+'\n')
output.close()

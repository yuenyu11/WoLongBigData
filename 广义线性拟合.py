# -*- coding: utf-8 -*-
__author__ = 'yuenyu111'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
def linear_model_main(X_parameters,Y_parameters,predict_value):
 # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
 #regr.coef_计算出的参数
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

def show_linear_line(X_parameters,Y_parameters):
 # Create linear regression object
    clf = Pipeline([('poly', PolynomialFeatures(degree=1)),
                    ('linear', LinearRegression(fit_intercept=False))])
    clf.fit(X_parameters[:np.newaxis], Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,clf.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

x=[]
y=[]
with open('F:/github/WoLongBigData/DataManager/weibo3794545218812248Width.txt', 'r') as f:
    for position, line in enumerate(f):
        t= line.strip().split('\t')
        x.append([float(t[1])])
        y.append(int(t[2]))
print(y[15])
x=x[:5]
y=y[:5]

clf = Pipeline([('poly', PolynomialFeatures(degree=1)),
                    ('linear', LinearRegression(fit_intercept=False))])
clf.fit(x[:np.newaxis], y)
print clf.predict(15)
# predictvalue = 15
# result = linear_model_main(x,y,predictvalue)
# print "Predicted value: ",result['predicted_value']
show_linear_line(x,y)
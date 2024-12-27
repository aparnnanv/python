# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:00:17 2024

@author: USER
"""
import pandas as pd
import numpy as np
data=pd.read_csv('D:\\STUDENTS\\aparnna\\iris.csv')
from sklearn.tree  import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=DecisionTreeClassifier(criterion='entropy')
model.fit(x_train,y_train)
pred=model.predict(x_test)
cm=confusion_matrix(y_test,pred)
acc=accuracy_score(y_test,pred)

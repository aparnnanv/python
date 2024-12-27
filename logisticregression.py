# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:24:26 2024

@author: USER
"""

import pandas as pd
import numpy as np
claimants=pd.read_csv("D:\\STUDENTS\\aparnna\\claimants.csv")
b=claimants.head(4)
claimants=claimants.drop(("CASENUM"),axis=1)
c=claimants.head(4)
k=claimants.isnull().sum()
t=claimants.mean()
v=claimants.CLMSEX.value_counts()
r=claimants.CLMSEX.value_counts().index[0]
claimants.iloc[:,0:4]=claimants.iloc[:,0:4].apply(lambda x:x.fillna(x.value_counts().index[0]))
claimants.CLMAGE=claimants.CLMAGE.fillna(claimants.CLMAGE.mean())
k=claimants.isnull().sum()
import statsmodels.formula.api as sm
logic_model=sm.logit("ATTORNEY~CLMSEX+CLMINSUR+SEATBELT+CLMAGE",data=claimants).fit()
w=logic_model.summary
y_pred=logic_model.predict(claimants)
claimants["pred_prob"]=y_pred
claimants["att_val"]=np.zeros(1340)
claimants.att_val
claimants.loc[y_pred>=0.5,"att_val"]=1
claimants.att_val

print(b,"\n")
print(c,"\n")
print(k,"\n")
print(t,"\n")
print(r,"\n")
print(v,"\n")
print(claimants,"\n")
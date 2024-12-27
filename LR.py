# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:09:48 2024

@author: USER
"""

import statsmodels.formula.api as smf
import pandas as pd
data=pd.read_csv("D:\\STUDENTS\\aparnna\\wc-at.csv")
d=data.columns
mod=smf.ols("AT~Waist",data=data).fit()
a=mod.summary()
pred=mod.predict(data.iloc[:,0])
                 
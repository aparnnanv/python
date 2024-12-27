# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:13:36 2024

@author: USER
"""

import pandas as  pd 
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("D:\\STUDENTS\\aparnna\\iris.csv")
z=data['SepalLengthCm'].mean()
z1=data['SepalLengthCm'].median()
z2=data['SepalLengthCm'].std()
z3=data['SepalLengthCm'].var()
z4=max(data['SepalLengthCm'])-min(data['SepalLengthCm'])
c=np.array(len(data))
p1=plt.bar(c,1)
plt.show()
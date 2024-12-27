# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:18:40 2024

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
np.random.seed(0)
data=np.random.multivariate_normal([0,0],[[1,0.75],[0.75,1]],100)
kmeans=KMeans(n_clusters=3)
kmeans.fit(data)
labels=kmeans.labels_
centers=kmeans.cluster_centers_
plt.scatter(data[:,0],data[:,1],c=labels)
plt.show()
# plt.scatter([centers[:,0],centers[:,1],c='yellow',marker='o',s=50,linewidths=10,edgecolors='blue','green'])
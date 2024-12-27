#pip install matplotlib
'''from matplotlib import pyplot as plt
Xpoints=[2,4,6]
Ypoints=[3,5,7]
plt.plot(Xpoints,Ypoints,'o',ms=10,mec="black",mfc="white")
plt.plot(Xpoints,Ypoints)
plt.show()'''

#sactterplot
'''import matplotlib.pyplot as plt
X=[1,2,3,4,5]
Y=[1,2,3.2,4.5,5]
plt.scatter(X,Y)
plt.show()'''

#barchart
'''import matplotlib.pyplot as plt
X=['A','B','C','D']
Y=[1,3,5,7]
plt.bar(X,Y)
plt.show()'''

#histogram
'''import matplotlib.pyplot as plt
import numpy as np
data=np.random.randn(1000)
plt.hist(data,bins=30)
plt.show()'''

#multipleplot
'''import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
z=[10,8,6,4,2]
plt.plot(x,y ,label='line 1')
plt.plot(x,z, label='line 2')
plt.legend()
plt.xlabel('employees')
plt.ylabel('salary')
plt.show()'''

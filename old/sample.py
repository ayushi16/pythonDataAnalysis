import csv
with open('../data/winequality-red.csv','r') as f:
	wines = list(csv.reader(f,delimiter=";"))

import numpy as np
wines = np.array(wines[1:], dtype=np.float)

import matplotlib.pyplot as mp
x=np.array(wines[:,8])
y=np.array(wines[:,1])
mp.plot(x,y)
mp.show()

/Users/hkevadia24/Desktop/ADT/numpy/working/data 




#print(wines.shape)
#print("Max pH")
#m =np.max(wines[:,8])
#print(m)




#q= [float(item[-1]) for item in wines[1:]]
#ql = sum(q) / len(q)
#print(ql)

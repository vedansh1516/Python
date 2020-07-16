
import numpy as np
a=np.matrix("1,2,3,4;4,5,6,7;4,5,6,7")
print(a)
w=a.shape
print(w[0])
print(w[1])
print(a.size)
b=np.matrix(np.arange(20,40)).reshape(5,4)
c=np.matrix(np.arange(25,50)).reshape(5,5)
p=np.matrix("3,1,2,3,2,5,6,7,8").reshape(3,3)
print(p)
q=np.matrix("x,y,z").reshape(3,1)
print(q)


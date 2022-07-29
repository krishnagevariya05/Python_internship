import numpy as np
import time
import sys

a=np.array([(1,2,3),(4,5,6)])
print(a)

"""Use less Memory"""
s=range(1000)
print(sys.getsizeof(5)*len(s))

t=np.arange(1000)
print(t.size*t.itemsize)

"""Use Less Time"""
SIZE =1000000
L1 = range(SIZE)
L2 = range(SIZE)

A1=np.arange(SIZE)
A2=np.arange(SIZE)
start = time.time()
result =[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)

start=time.time()
result=A2+A1

print((time.time()-start)*1000)

"""Numpy Operation"""

"""To calculate dimension of array"""
import numpy as np
a= np.array([(1,2,3),(4,5,6)])


print(a.ndim)
"""To know size of item in array"""
print(a.itemsize)
"""To know type of item in array"""
print(a.dtype)
"""To find size of numpy array"""
print(a.size)  #NUmber of element
"""To find shape of numpy array"""
print(a.shape) #row and column
"""Slicing"""
print(a[0,2])
print(a[0:,2])
"""Min"""
print(a.min())
"""Max"""
print(a.max())
"""Sum"""
print(a.sum())
"""Sum of axis 0"""
print(a.sum(axis=0))
"""Sum of axis 1"""
print(a.sum(axis=1))
"""Square root of numpy array"""
print(np.sqrt(a))
"""standard deviation"""
print(np.std(a))
"""Reshap"""
print(a)
a=a.reshape(3,2)
print(a)

b=np.linspace(1,3,10)
print(b)

"""Matrix Addition"""
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print("Addition: ",a+b)
"""Matrix Subtraction"""
print("Subtraction: ",a-b)
"""Matrix Multiplication"""
print("Multiplication: ",a*b)
"""Matrix Division"""
print("Division: ",a/b)
"""Vertical stacking"""
print(np.vstack((a,b)))
"""Horizontal stacking"""
print(np.hstack((a,b)))
"""Convert in Single column"""
print(a.ravel())

"""Exponential value"""
ar = np.array([(1,2,3),(4,5,6)])
print(np.exp(ar))

"""Log value"""
print(np.log10(ar))





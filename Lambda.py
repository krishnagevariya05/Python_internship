#lambda arguments:expression

x = lambda a:a*a
print(x(3))

def new(a):
    return a*a
print(new(3))


def A(x):
    return(lambda y:x+y)
t=A(4)
print(t(8))

#lambda within filter()
mylist=[1,2,3,4,5,6]
new_list=list(filter(lambda a:a/3==2,mylist)) #Syntax: filter(function, iterables)
print(new_list)

def new1( i):
    if i>=3:
        return i
j=filter(new1,[1,2,3,4])
print(list(j))

#lambda within map()
p=list(map(lambda a:a/3!=2,mylist))   #Syntax: map(function, iterables)
print(p)
def new(a):
    return a*a
p=list(map(new,[1,2,3,4]))
print(p)

def new(a,b):
    return a*b
p=list(map(new,[1,2,3,4],[2,3,4,5]))
print(p)

#lambda within reduce()
#synatax: reduce(function, sequence)
from  functools import reduce   #from functools import *
print(reduce(lambda a,b: a+b, [23,26,46,98,1]))

def new2(x,y):
    return x+y
s=reduce(new2,[1,2,3,4])
print(s)


"""Lambda for algebra"""
#linear equations
s=lambda a:a*a
print(s(4))

#3x+4y
d=lambda x,y: 3*x + 4*y
print(d(4,7))

#Quadratic equation
x=lambda a,b: (a+b)**2
print(3,4)

#filter within map function
c=list(map(lambda x:x+x,filter(lambda x:x>=4,[2,3,4,5])))
print(c)

#map within filter function
z=list(filter(lambda a:a>=2,map(lambda a:a*a,[0,1,2,3])))
print(z)

#map, filter within reduce function
s=reduce(lambda a,b:a*b,map(lambda a:a+a,[1,2,3]))
print(s)
t=reduce(lambda a,b:a*b,filter(lambda b:b>=2,[1,2,3,4]))
print(t)
r=reduce(lambda a,b:a*b,map(lambda a:a+a,filter(lambda a:a>=2,[1,2,3,4])))
print(r)



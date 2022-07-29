def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:"Hi",2:"Hello"}
b=new(a)
print(b)
print(next(b))
print(next(b))

def myfunc(i):
    while i<=3:
        yield i
        i=i+1
j=myfunc(2)
print(next(j))
print(next(j))

def ex():
        n=3
        yield n
        n=n*n
        yield n

v=ex()
print(next(v))
print(next(v))

#Generators with loops
def ex():
    n = 3
    yield n
    n = n * n
    yield n
v=ex()
for x in v:
    print(x)

#Generator Expression
f=range(6)
print("List comp",end=":")
q=[x+2 for x in f]
print(q)
print("Generator expression",end=":")
r=(x+2 for x in f)
for x in r:
    print(x)



# #Fibonacci series
# def feb():
#     f,s=0,1
#     while True:
#         yield f
#         f,s=s,f+s
#
# for x in feb():
#     if(x>50):
#         break
#     print(x, end=" ")
#
# #Number stream
# a=range(100)
# b=(x for x in a)
# print(b)
# for y in b:
#     print(y)
#
# a=range(2,100,2)
# b=(x for x in a)
# print(b)
# for y in b:
#     print(y)

# #sinewave
# import numpy as  np
# from matplotlib import pyplot as plt
# import seaborn as sb
# def s(flip=2):
#     x=np.linspace(0,14,100)
#     for i in range(1,5):
#         plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
#
# sb.set()
# s()
# plt.show()
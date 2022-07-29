import Module as md   #from Module import *
addition = md.add(10,15)
subtraction = md.sub(20,10)
multiplication = md.mul(1,2)
divison = md.div(4,2)
print("Addition: ",addition)
print("Subtraction: ",subtraction)
print("Multiplication: ",multiplication)
print("Divison: ",int(divison))

from sample import *
print(fact(5))
print(pal('151'))

import sample
print(dir(sample))

import Module
print(dir(Module))

import sys
print(sys.path)

import math
print(math.factorial(10))

import random
print(random.randrange(0,50))

import datetime
print(datetime.date.today())
print(datetime.datetime(2020,6,7,4,30,54,678))
print(datetime.datetime.today())
print(datetime.datetime.now())
v=datetime.datetime.now()
print(v.year,v.month, v.hour)
print(datetime.date(2020,7,5))
print(datetime.date(3,45,23))
b1=datetime.timedelta(days=20)
b2=datetime.timedelta(days=30)
b3=b1-b2
print(b3)
print(type(b3))
import time
print(time.time())
print(time.ctime(1652850972.833709))
print(help(time.time()))
print(time.localtime())
a=time.localtime()
b=time.mktime(a)
print(b)
c=time.asctime(a)
print(c)
x=time.strftime("%m/%d/%y")
print(x)
y="05 November 2001"
s=time.strptime(y,"%d %B %Y")
print(s)
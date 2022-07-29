# import array
# a=array.array('i',[1,2,3,4,5])
# print(a)

# from array import *
# a=array('i',[1,2,3,4,5])
# print(a)

import array as arr
a=arr.array('i',[1,2,3,4,5])
print(a)
print(a[2])
print(len(a))

a.append(6)
print(a)
a.extend([7,8,9])
print(a)
a.insert(0,0)
print(a)

#Array Deletion
print("Popping last element: ",a.pop())
print("Popping 0th element: ",a.pop(0))
a.remove(2)
print(a)
a.pop(-3)
print(a)

#Array Concetanation
p=arr.array('d',[1.1,1.2,1.3,1.4])
q=arr.array('d',[2.1,2.2])
r=arr.array('d')
r=p+q
print(r)

#Array Slicing
print(a[0:5])
print(r[0:-2])
print(r[::-1])
print(r)

#Looping in Array
print("for loop1")
for i in a:
    print(i)
print("for loop1")
for i in a[0:3]:
    print(i)

print("While loop1")
temp=0
print(a)
while temp<a[3]:
    print(a[temp])
    temp+=1
print("While loop2")
tem=0
while tem<len(a):
    print(a[tem])
    tem+=1
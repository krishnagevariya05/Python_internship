"""
1.Arithmetic
2.Assignment
3.Comparison
4.Logical
5.Membership
6.identity
7.Bitwise
"""
#Arithmetic
x=10
y=20
print("Addition: ",x+y)
print("Subtraction: ",x-y)
print("Multiplication: ",x*y)
print("Exponential: ",x**y)
print("Divison: ",x/y)
print("flor Divison: ",x//y)
print("Modulo: ",x%y)

#Assignment
a=5
a+=5
print("+= :",a)
a**=5
print("**= :",a)

#Comparison
val=10
num=20
compare= val==num
print(compare)

#Logical
p=10
print("AND: ", x>10 and x>5)
print("OR: ", x>10 or x>5)
print("NOT: ", not (x>10 or x>5))


#identity
list1=[10,20,30]
list2=[10,20,30]
print(list1 is list2)
print(list1 is not list2)

#Membership
print("Membership Operator")
print(list1 in list2)
print(10 in list1)
print(list1 not in list2)
print([10,20,30] in list1)

#Bitwise
print("Bitwise AND: ",10 & 12)
print("Bitwise OR", 10 | 12)
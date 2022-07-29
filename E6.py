a="Hello World"
print("Reverse String: ",a[::-1])

"""Count the string"""
print("Count the string: ",a.count(a))

"""Find len of string"""
print("Length of string: ",len(a))

"""Reverse Array"""
arr=[1,2,3,4,5]
print("Reverse Array: ",arr[::-1])

"""Float to int"""
p=1.22
print("Float to int: ",int(p))

"""Convert number into hex"""
num=8
print("Hex Number: ",hex(num))

"""Count Vowel"""
s1="abceio"
v=0
for i in s1:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v=v+1

print("Total Vowel in String: ",v)

"""String Opposite case"""
str="Hello"
print(str)
print(str.upper())
print(str.lower())
print(str.swapcase())


"""Print Hello world"""
print("hello", end=" ")
print("world")


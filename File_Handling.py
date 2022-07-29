""" File Handling Example 1"""
import os
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","w")
file.close()

""" File Handling Example 2"""
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","r")
print(file.read())
file.close()

""" File Handling Example 3"""
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","r")
print(file.read(5))
file.close()

""" File Handling Example 4"""
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","r")
print(file.readline())
file.close()

""" File Handling Example 5"""
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","r")
print(file.readlines())
file.close()

""" File Handling Example 6"""
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","r")
print(file.readline(2))
file.close()

""" File Handling Example 7"""
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","r")
for line in file:
    print(file.readlines())
file.close()



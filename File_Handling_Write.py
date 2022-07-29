""" File Handling - Write Example 1"""
import os
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","w")
file.write("Hello World!!")
file.write("Hello World again?")
file.close()

""" File Handling - Write Example 2"""
file=open("C:/Users/d/PycharmProjects/pythonProject1/t1.txt","w")
file.write("Oops Owerwrite!!")
file.close()

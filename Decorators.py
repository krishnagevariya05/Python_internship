"""1. Example"""
# def function1(function):
#     def wrapper():
#         print("Hello")
#         function()
#         print("Welcome to the python world")
#     return wrapper
# @function1
# def function2():
#     print("pythoninsta")
#
# # function2 = function1(function2)
#
# function2()

"""2. Example"""
def function1(function):
    def wrapper(*args, **kwargs):
        print("Hello")
        function(*args, **kwargs)
        print("Welcome to the python world")
    return wrapper
@function1
def function2(name):
    print(f"{name}")

# function2 = function1(function2)

function2("Krishna")

"""3. Example"""
def function1(function):
    def wrapper(*args, **kwargs):
        print("Hello")
    return wrapper
@function1
def function2(name):
    print(f"{name}")

function2("Python")

"""Fancy Decorators"""

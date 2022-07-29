"""First class Object"""
def fun1(name):
    return f"Hello, {name}"
def fun2(name):
    return f"{name}, How are you"
def fun3(fun4):
    return fun4("Dear Learner")
print(fun3(fun1))
print(fun3(fun2))

"""Inner Function"""
def func1():
    print("first Function")
    def func2():
        print("fisrt child function")
    def func3():
        print("Second child function")
    func2()
    func3()
func1()


def funct(n):
    def funct1():
        return "Python"
    def funct2():
        return "ML"
    if n==1:
        return funct1()
    else:
        return funct2()
a=funct(1)
b=funct(2)
print(a)
print(b)
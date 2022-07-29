"""Single Inheritance"""
print("Single Inheritance\n")
class parent:
    def fun1(self):
        print("This is func1")

class child(parent):
    def fun2(self):
        print("This is func2")

ob= child()
ob.fun1()

"""Multiple Inheritance"""
print("Multiple Inheritance\n")
class parent:
    def fun1(self):
        print("This is func1")

class parent2:
    def fun3(self):
        print("This is func3")

class child(parent,parent2):
    def fun2(self):
        print("This is func2")

ob= child()
ob.fun3()


""" Multiple Inheritance"""
print("Multiple Inheritance\n")
class parent:
    def fun1(self):
        print("This is func1")

class parent2(parent):
    def fun3(self):
        print("This is func3")

class child(parent2):
    def fun2(self):
        print("This is func2")

ob= child()
ob.fun3()
ob.fun1()

"""Hirerchical Inheritance"""
print("Hirerchical Inheritance\n")
class parent:
    def fun1(self):
        print("This is func1")

class parent2(parent):
    def fun3(self):
        print("This is func3")

class child(parent):
    def fun2(self):
        print("This is func2")

ob= child()
ob2=parent2()
ob2.fun1()
ob.fun1()

"""Hybrid Inheritance"""
print("Hybrid Inheritance\n")
class parent:
    def fun1(self):
        print("This is func1")

class parent2(parent):
    def fun3(self):
        print("This is func3")

class parent3:
    def fun4(self):
        print("This is func4")

class child(parent,parent3):
    def fun2(self):
        print("This is func2")

ob= child()
ob.fun4()
ob.fun1()

"""Super function"""
print("Super function\n")
class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        super().func1()
        print("This is function 2")

obj=Child()
obj.func2()

"""Method Overriding"""
print("Method Overriding\n")
class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func1(self):
        print("This is function 2")

obj=Child()
obj.func1()



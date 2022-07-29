#Python abs() function:
integer = -20
print('Absolute value of -40 is:', abs(integer))
#Python all() function:
# all values true
k = [1, 3, 4, 6]
print(all(k))
# all values false
k = [0, False]
print(all(k))
# one false value
k = [1, 3, 7, 0]
print(all(k))
# one true value
k = [0, False, 5]
print(all(k))
# empty iterable
k = []
print(all(k))

#Python bin() function:
x =  10
y =  bin(x)
print (y)

#Python callable() function:
x = 8
print(callable(x))

#Python getattr() function:
class Details:
    age = 22
    name = "Phill"


details = Details()
print('The age is:', getattr(details, "age"))
print('The age is:', details.age)

#Python hasattr() function:
l = [0, False, 5]
print(any(l))

l = []
print(any(l))

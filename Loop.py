"""
1. While
2. For
3. Nested
"""
#While
count=0
while count<9:
    print("Number: ", count)
    count=count+1

import random
n=20
to_be_guessed = int(n*random.random())+1
guess=0
while guess != to_be_guessed:
    guess =int(input("New Number: "))
    if guess>0:
        if guess > to_be_guessed:
            print("Number too large!!")
        elif guess < to_be_guessed:
            print("Number too small!!")
    else:
        print("Sorry that you are giving up!")
        break
else:
    print("Congratulation. You made it!")

#For loop
n=int(input())
f=1
if n<0:
    print("Number is Nagative.")
elif n==0:
    print("Factorial: ",f)
else:
    for i in range(1,n+1):
        f*=i
print("Factorial: ",f)



#pyramid
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*", end=" ")
        print("\r")
pattern(5)

#inverse pyramid
def patter1(n):
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("*", end=" ")
        print("\r")
patter1(5)

#right start pattern
def pattern2(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
pattern2(5)
print("\n")
print("\n")
#left start pattern
def pattern3(n):
    k=2*n -2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
    k =- 1
    for i in range (n-1, -1, -1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+2
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
pattern3(5)
print("\n")
print("\n")

#Hourglass pattern
def pattern4(n):
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")
    k = 2 * n - 2
    for i in range(0, n+1):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")
pattern4(5)

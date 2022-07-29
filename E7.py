
list1=["a","b","d","e"]
list2=[1,2,3,4]
dic={}
for i in list1:
    for j in list2:
        dic[i]=j
        list2.remove(j)
        break

print(dic)

def function1(function):
    def wrapper(*args, **kwargs):
        print("Name is:", end=" ")
        function(*args, **kwargs)
        print("Thank you")
    return wrapper
@function1
def function2(name):
    print(f"{name}")

# function2 = function1(function2)

function2("Krishna")

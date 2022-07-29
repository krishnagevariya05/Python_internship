def bubble_sort(list1):
    count = 0
    c=0
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if (list1[j]>list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
                count=count+1
        c=c+1

    print("Number of Passes: ",c)
    print("Number of Iteration: ",count)
    return list1


list1=[94,64,10,43,5]
print("Unsorted list is: ",list1)

print("Sorted list is: ",bubble_sort(list1))
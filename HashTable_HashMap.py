
my_dict={'Krishna':'001','Harshil':'002','Dharmik':'003'}
print(my_dict)
print(type(my_dict))

new_dict=dict()
print(new_dict)
print(type(new_dict))

#Nested Dictionaries
emp_details={'Employee':{'Dev':{'ID':'001','Salary':'20000'},
                         'Eva':{'ID':'002','Salary':'30000'}}}
print(emp_details)

#Accessing Values
#1. Using Parameter
print(my_dict['Krishna'])

#2. Using Function
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Harshil'))

#3. Using for loop
for i in my_dict:
    print(i)
for i in my_dict.values():
    print(i)
for i in my_dict.get('Krishna'):
    print(i)
for i,j in my_dict.items():
    print(i,j)


#Updating Values
my_dict['Krishna']='000'
my_dict['Rency']='001'
print(my_dict)

#Deleting item
print(my_dict.pop('Harshil'))
print(my_dict.popitem())
print(my_dict.pop('Dharmik'))
del my_dict['Krishna']
print(my_dict)


#convert dictionary into a dataframe




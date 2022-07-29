import os
# file=open("Hello.txt",'x')
# file.close()

file=open("Hello.txt",'w')
file.write("Python is AWS")
file.close()

file=open("Hello.txt",'r')
print(file.readline())
file.close()

if os.path.exists("Hello.txt"):
  os.remove("Hello.txt")
else:
  print("The file does not exist")
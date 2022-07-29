string = "Hello World!!"
print("The original string: " + string)
p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for i in string:
    if i in p:
        string = string.replace(i, "")
print("The string after punctuation: " + string)
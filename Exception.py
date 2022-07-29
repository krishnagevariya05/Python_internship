import sys


def linux_interaction():
    assert ('linux' in sys.platform), "function can run only on Linux system."

try:
    linux_interaction()
except:
    print("linux function was not executed")

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("The linux_interaction() function was not executed")
else:
    print("Executing the else clause.")
finally:
    print("Cleaning up, irrespective of any exceptions.")


try:
    with open('file.log') as file:
        read_data =file.read()
except:
    print("Could not open file.log") #File does not exist.....


try:
    linux_interaction()
    with open('file.log') as file:
        read_data =file.read()
except AssertionError as error:
    print(error)
    print("The linux_interaction() function was not executed")
except FileNotFoundError as file_error:
    print(file_error)
    print("Could not open file.log")


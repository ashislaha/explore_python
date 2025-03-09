def sum(num1, num2):
    try:
        return num1+num2
    except:
        print("one of them are not in supported number format")
    else:
        print("No error found")

input1 = input("Enter a number")
sum(input1, 10)

def file_operation():
    try:
        file = open("ab.txt", "r") # file does not exist, so reading it will throw an error
        content = file.read()
        print(content)
    except OSError:
        print("There is an OS error")
    except:
        print("File open error")

file_operation()
def sum(num1, num2):
    try:
        return num1+num2
    except:
        print("one of them are not in supported number format")
    else:
        print("No error found")

def file_operation():
    try:
        file = open("ab.txt", "r") # file does not exist, so reading it will throw an error
        content = file.read()
        print(content)
    except OSError:
        print("There is an OS error")
    except:
        print("File open error")
    finally:
        print("File handling is done")


def scan_a_number():
    while True:
        try:
            number = int(input("Enter a number: "))
        except:
            print("Please enter a number!!!")
            continue
        else:
            print(number)
            break # user enters a valid number
        finally:
            print("scanning is completed")

if __name__ == "__main__":
    input1 = input("Enter a number")
    sum(input1, 10)
    file_operation()
    scan_a_number()
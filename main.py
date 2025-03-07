import datetime
import json
import os

import matplotlib
import matplotlib.pyplot as plot
import numpy as np

# formatting string
name = "Ashis"
print("Hello {}".format(name))
print(f"Hello {name}")

# function
def printMe(name="Ashis"):
    print(f"My name is {name}")

printMe('aheli')

# multiple arguments function
def myfunc(*args):
    # return 5% of all numbers sum
    # args is tuple of all those inserted numbers for *args
    print(args)
    return sum(args) * 0.05
print(myfunc(100,200,300,400))

def fruitsChecking(**key_args):
    # args is dictionary type now, we can pass keyward arguments
    print(key_args)
    if "fruits" in key_args:
        fruitValue = key_args["fruits"]
        print(f"Fruit is present - {fruitValue}")
    else:
        print("Fruit is not present here")
fruitsChecking(flowers ="lilly",fruits = "mango")

# map function - lambda
def square(num): 
    return num**2
numbers = [1,2,3,4,5]
new_numbers = list(map(square, numbers))
for item in new_numbers:
    print(item)

square = lambda num: num **2
print(f"square of 5 = {square(5)}")

even_numbers_only = list(filter(lambda num: num%2 == 0, [1,2,3,4,5,6,7,8,9]))
print(f"Even numbers only {even_numbers_only}")

# Take input from keyboard

def greet(message):
    print(message)
    pass

message = input("what you want to greet? ")
greet(message)

birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year) # similarly we have float(), bool(), str()
print("age = ", age)

# explore little bit on string
test_string = "this is a test string"
print(test_string.upper())

find_test = test_string.find("test")
print(find_test)

replace_string = test_string.replace("test", "new")
print(replace_string)

# in operator to find out - contains
is_present = "is" in test_string
if is_present:
    print(is_present)

# it uses >, >=, <, <=, ==, != for compare
# it uses "or", "and", "not" for logical operator

price = 500
if (price >= 40 and price <= 60):
    print("price is within 40 and 60")
elif (price >= 60 and price <= 100):
    print("Price is within 60 and 100")
else:
    print("price is not within 40 and 100")

# 1. ---> List
names = ["ashis", "aheli", "barnali", "tanish", "chandana", "diya"] # list
print(names)
print("-1 position name is the last object", names[-1])
print(names[1:3]) # it will return from ith index to jth index, not included the jth index element.

names.append("navya")
names.insert(0, "rrrr") # use "remove(element)" or clear() to remove or clear the list
print(len(names))

for (index, item) in enumerate(names):
    print(index, item)
print("\n")

fruits = ["apple", "mango", "banana"]
colors = ["red", "orange", "yello"]
for item in zip(fruits, colors):
    print(item)
print("\n")

#List comprehension
print("List comprehension")
letters = [x for x in "abcdefgh"]
print(letters)
print("\n")

divisibleBy3 = [x for x in range(1,51) if x % 3 == 0]
print(divisibleBy3)
print("\n")

# iterate over a list
for name in names:
    print(name)

print("using while loop")
i = 0
while i < len(names):
    print(names[i])
    i += 1

# range function
numberList = range(5, 10, 2) # excluding the end number of the range, 2 is step
for num in numberList:
    print(num)

# 2. ---> tuple, they are immutable
numberTuple = (1,2,3)
print(len(numberTuple))

# 3. ----> dictionary
studentsDict = {
    "1" : { "name": "Ashis", "address": "India" },
    "2": { "name": "Barnali", "address" : "India" },
    "3": { "name": "Aheli", "grade": "6"}
}
studentsDict["100"] = {"name": "x1", "address": "x2"}
studentsDict.update({"101": {"name": "y1", "address": "y2"}})

for key, value in studentsDict.items():
    print(key, value)

# 4. ----> class, inheritance, polymorphism
class Person:
    def __init__(self, name, address, dob):
        self.name = name
        self.address = address
        self.dob = dob
    def __str__(self):
        return f"Name is {self.name} and address is in {self.address}, born in {self.dob}, age = {self.age()}"

    def age(self):
        # get current year and return year - dob
        currentTime = datetime.datetime.now()
        return currentTime.year - int(self.dob)

person = Person("Ashis", "India", "1989")
print(person)

class ChildPerson(Person):
    def __init__(self, name, address, dob, school):
        super().__init__(name, address, dob)
        self.school = school
    
    # polymorphism -- override __str__(self) and update string of the subclass.
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} , school is at {self.school}"
    
child = ChildPerson("Aheli", "India", "2013", "Inglewood middle school")
print(child)
        
# 5. ----> JSON 

# JSON to Dictionary
jsonString = '{"type": "Electronics", "computer": "MacBook", "RAM": "16 GB"}'
jsonDict = json.loads(jsonString)

print(jsonDict)

# Dictionary to JSON
jsonString_again = json.dumps(jsonDict)
print(jsonString_again)

# 6. File system (try except finally)
# try-except-finally
# there are 4 modes to open a file
# r - read
# w - write
# a - append
# x - create if file does not exist
# and there are 2 types of file - binary file, text file
# default is "rt"
try:
    f = open("abc.txt", mode="at")
    try:
        f.write(" appending content ")
    except:
        print("error while writing into file")
    finally:
        f.close() 
except:
    print("error while opening file")

# read file

try:
    file = open("abc.txt", mode="rt")
    content = file.read()
    print(content)

except:
    print("error while opening text file")
finally:
    file.close()

# remove file
if os.path.exists("test_abc.txt"):
    os.remove("test_abc.txt")


# 7. matplot
print("matplot version ", matplotlib.__version__)

# 8. numpy
# numpy has more types called dtype
# we can copy / view a numpy array

print("Numpy version ", np.__version__)
arr = np.array([[1,2,3,4], [10, 20, 30, 40]])
print("input array dimention -->", arr.ndim)


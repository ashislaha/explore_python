import math
import pdb
import random

def generate_random_between_range(a,b):

    # if we want to generate same series of random number, assign a starting seed point
    # random.seed(42)

    print(f"lower limit = {a} upper limit = {b}")
    random_num = random.randint(a, b)
    print(random_num)
    return random_num

def choose_random_in_a_list(mylist):
    print(random.choice(mylist))
    print(random.sample(mylist, k=2))

def test_python_debugger():
    x = [1,2]
    y = 5
    z = 6
    a = y + z 
    try:
        pdb.set_trace() # python debugger and can explore different values, use "q" to exit debugger
        b = x + y # throw an error here
    except:
        print("exception occurs")

if __name__ == "__main__":
    generate_random_between_range(1,100)
    choose_random_in_a_list(list(range(10)))
    test_python_debugger()


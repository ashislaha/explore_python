# how to calculate time taken by python function (time profile)
# tracking time elapse
# using timeit module
# special %%timeit magic for jupiter notebook

import time
import timeit
import textwrap

def func_one(n):
    arr = []
    for num in range(n):
        arr.append(str(num))
    return arr

def func_two(n):
    return list(map(str,range(n)))

if __name__ == "__main__":
    # current time
    start_time = time.time()
    # Run code
    func_one(1000000)
    # curren time after running code
    end_time = time.time()
    # elapsed time
    print(f"func_one takes {end_time-start_time}")

    # current time
    start_time = time.time()
    # Run code
    func_two(1000000)
    # curren time after running code
    end_time = time.time()
    # elapsed time
    print(f"func_one takes {end_time-start_time}")

    # statement is calling over and over again
    statement = textwrap.dedent('''
    func_one(100)
    ''')
    # it is getting called only once
    set_up = textwrap.dedent('''
    def func_one(n):
        arr = []
        for num in range(n):
            arr.append(str(num))
        return arr
    ''')
    timeit.timeit(statement,set_up,number=10000)
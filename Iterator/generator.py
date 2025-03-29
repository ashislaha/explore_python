# generator can generate on fly using yield and it optimize memory

def generate_num(number):
    for i in range(number):
        yield i

def print_num():
    num_generator = generate_num(10)
    # you can iterate through it
    print(num_generator)
    print(next(num_generator))
    print(next(num_generator))

def iterator_of_input(input):
    input_generator = iter(input)
    print(next(input_generator))
    print(next(input_generator))

def square(upto):
    for i in range(upto):
        yield i**2

def generate_square():
    input_num = int(input("Enter a positive number "))
    for square_num in square(input_num):
        print(square_num)


if __name__ == "__main__":
    print_num()
    iterator_of_input("apple")
    generate_square()
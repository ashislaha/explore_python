# in decorator we are passing a function to an another to decorate it

def main_function():
    print("This is main function")
    
def decorated_function(original_func):
       
    def wrap_func():
        print("Do preprocessing in decorated func")
        original_func()
        print("Do post processing in decorated func")
        
    return wrap_func

# we can do the same using @
@decorated_function
def another_func():
    print("Another func")     
    
if __name__ == "__main__":
    main_function()
    wrapped = decorated_function(main_function)
    wrapped()
    another_func()
import re

input_string = """
    this is random content having contact number 445-555-6666. 
    You can use regular expression to find out multiple contact numbers.
    I have one dog at home.
"""

def explore_regular_expression_phone_number():
    # pattern = r"(/d/d/d)-/d/d/d-/d/d/d/d"
    pattern = r"\d{3}-\d{3}-\d{4}"
    print("contact" in input_string)
    pattern_contact = "contact"
    match = re.search(pattern_contact, input_string)
    matches = re.findall(pattern_contact, input_string)
    print(match.span())
    print(matches)
    number_match = re.search(pattern,input_string)
    print(number_match)
    print(number_match.group())
    # use compile to adjust multiple pattern and do search 

def choose_alternative():
    pattern = r"cat|dog"
    print(re.search(pattern,input_string))
    print(re.findall(pattern,input_string))
    print(re.findall(r'^\d', '1 is starting of positive odd'))
    print(re.findall(r'\d$','ending with 1'))

def remove_number():
    pattern = r"[^\d]+" # exclude digits (one or more)
    print(re.findall(pattern, input_string))

def filter_with_hiphen():
    pattern = r"[\w]+-[\w]+" # exclude digits (one or more)
    print(re.findall(pattern, "this has few content with hiphen hi-hello one-two"))

if __name__ == "__main__":
    explore_regular_expression_phone_number()
    choose_alternative()
    remove_number()
    filter_with_hiphen()
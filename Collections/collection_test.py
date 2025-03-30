from collections import Counter
from collections import defaultdict
from collections import namedtuple

def countDuplicates(input):
    frequency = Counter(input)
    print(frequency)

def default_dict_test():
    dict = {"a": 1}
    print(dict["a"])
    # get a KeyError if key does not present in dict like dict["b"]

    # you can use default dictionary, if there is no key, it assign a default value
    d = defaultdict(lambda: 0)
    d["a"] = 1
    print(d["b"])

def test_named_tuple():
    normal_tuple = (10,11,12)
    print(normal_tuple[0])

    # you can define value to a name using named tuple, easy to access
    Dog = namedtuple("Dog", ["name", "age", "breed"])
    sammy = Dog(name="Samm", age=2, breed="Husky")
    print(f"Dog name is{sammy.name}, age = {sammy.age}" )


if __name__ == "__main__":
    countDuplicates([1,1,1,1,2,2,2,2,2,2,3,4,5,6,7,7,7,7])
    default_dict_test()
    test_named_tuple()

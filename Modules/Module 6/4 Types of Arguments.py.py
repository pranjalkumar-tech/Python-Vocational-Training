# Types of Arguments

# Positional Arguments
def student(name, age):  # 'name' and 'age' are parameters
    print("Name:", name)
    print("Age:", age)
student("Pranjal", 20)  # Values are passed according to their position


# Keyword Arguments
student(age=20, name="Pranjal")  # Values are passed using parameter names


# Default Arguments
def greet(name="User"):  # "User" is the default value
    print("Hello", name)
greet()  # Uses the default value
greet("Pranjal")  # Uses the given value


# Variable Length Arguments
def numbers(*args):  # *args accepts multiple arguments
    print(args)
numbers(10, 20, 30, 40)


# Keyword Variable Length Arguments
def details(**kwargs):  # **kwargs accepts multiple keyword arguments
    print(kwargs)
details(name="Pranjal", age=20, course="Python")
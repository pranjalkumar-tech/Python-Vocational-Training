# Constructor
# A constructor is a special method that is automatically called
# when an object is created.

# __init__() is used as a constructor.

class Student:
    def __init__(self, name, age):  # Constructor
        self.name = name  # Stores the name
        self.age = age  # Stores the age

student1 = Student("Pranjal", 20)  # Creates an object

print(student1.name)
print(student1.age)
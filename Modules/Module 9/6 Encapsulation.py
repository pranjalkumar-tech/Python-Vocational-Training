# Encapsulation
# Encapsulation means keeping data and methods together inside a class.
# A private variable can be created using double underscore.

class Student:
    def __init__(self, name, age):
        self.name = name  # Public variable
        self.__age = age  # Private variable

    def display(self):
        print("Name:", self.name)
        print("Age:", self.__age)

student = Student("Pranjal", 20)
student.display()
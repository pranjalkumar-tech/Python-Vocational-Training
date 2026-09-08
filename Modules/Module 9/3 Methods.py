# Methods
# A method is a function defined inside a class.

class Student:
    def __init__(self, name):  # Constructor
        self.name = name  # Stores the name

    def display(self):  # Creates a method
        print("Name:", self.name)

student1 = Student("Pranjal")  # Creates an object
student1.display()  # Calls the method
# Class and Instance Variables

class Student:
    school = "ABC School"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable

student1 = Student("Pranjal", 20)
student2 = Student("Rahul", 21)

print(student1.name)
print(student2.name)

print(student1.school)
print(student2.school)
# Inheritance
# Inheritance allows one class to use the properties and methods
# of another class.

class Animal:
    def eat(self):  # Method of parent class
        print("Animal is eating")

class Dog(Animal):  # Dog inherits Animal
    def bark(self):  # Method of child class
        print("Dog is barking")

dog = Dog()

dog.eat()  # Uses parent class method
dog.bark()  # Uses child class method
# Polymorphism
# Polymorphism means the same method name can have different behaviour.

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.sound()  # Calls Dog's sound method
cat.sound()  # Calls Cat's sound method
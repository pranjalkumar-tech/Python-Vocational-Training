# Scope

# Local Scope
def greet():
    name = "Pranjal"  # Local variable
    print(name)
greet()

# Global Scope
name = "Pranjal"  # Global variable
def greet():
    print(name)  # Accessing the global variable
greet()
print(name)
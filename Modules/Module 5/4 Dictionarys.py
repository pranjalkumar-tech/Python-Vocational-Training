# Dictionary
student = {
    "name": "Pranjal",
    "age": 20,
    "course": "Python"
}
print(student)

# Accessing values
print(student["name"])
print(student["age"])

# Adding a new item
student["city"] = "Delhi"
print(student)

# Changing a value
student["age"] = 21
print(student)

# Removing an item
student.pop("city")
print(student)
#__________________________________________________________________________________________________________________________________________________________________________

# Dictionary Methods
student = {
    "name": "Pranjal",
    "age": 20,
    "course": "Python"
}

# keys()
print(student.keys())  # Returns all the keys 

# values()
print(student.values())  # Returns all the values

# items()
print(student.items())  # Returns all key-value pairs

# get()
print(student.get("name"))  # Returns the value of a key

# update()
student.update({"age": 21})  # Updates the dictionary
print(student)

# clear()
student.clear()  # Removes all items from the dictionary
print(student)
#__________________________________________________________________________________________________________________________________________________________________________

# Nested Dictionary
# A dictionary can contain another dictionary.
students = {
    "student1": {
        "name": "Pranjal",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}
print(students)

# Accessing values from a nested dictionary
print(students["student1"]["name"])
print(students["student2"]["age"])
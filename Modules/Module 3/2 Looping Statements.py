# Type of Control Statements

# Looping Statements
"""1.  while Loop:
# Step 1: Initialization
variable = starting_value
# Step 2: Condition
while condition:
    # Step 3: Code to repeat
    # Code
    # Step 4: Update
    variable = variable + 1 or -1, *2, etc."""

# Show numbers from 1 to 5
number = 1
while number <= 5:
    print(number)
    number += 1

# Show numbers from 10 to 1
number = 10
while number >= 1:
    print(number)
    number -= 1
# __________________________________________________________________________________________________________________________________________________________________________


"""For Loop:
for variable in range(start, stop, step):
    # Code"""

# Show number from 0 to 5
for num in range(5):
    print(num)

# Show number from 1 to 5
for num in range(1, 6):  # Start = 1, Stop = 6
    print(num)

# show even number from 2 to 10
for number in range(1, 11, 2):
    print(number)
# __________________________________________________________________________________________________________________________________________________________________________


# Break Statement (Stops):
# Using this in a for loop:
for number in range(1, 11, 1):
    if number == 5:
        break
    print(number)

# Using this in a while loop:
number = 0
while number <= 10:
    if number == 5:
        break
    number += 1
    print(number)
# __________________________________________________________________________________________________________________________________________________________________________


# Continue Statemrnt (Skip):
# in for loop:
for num in range(1, 11, 1):
    if num == 3:
        continue
    print(num)

# in while loop:
num = 0
while num <= 10:
    if num == 4:
        num += 1
        continue
    print(num)
    num += 1
# __________________________________________________________________________________________________________________________________________________________________________


# Pass Statement:
count = 0  # Starting value
while count <= 3:  # Run while count is less than or equal to 3
    pass  # Do nothing
    count += 1
print("Done")  # Print after the loop finishes
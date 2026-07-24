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
    variable = variable + 1    # or -1, *2, etc."""

# Show numbers from 1 to 5
number = 1
while number <= 5:
    print(number)
    number += 1

# Show numbers from 10 to
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

import random  # Imports the random module

secret_number = random.randint(1, 100)  # Generates a random number
attempts = 0  # Stores the number of attempts

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))  # Takes user's guess
    attempts = attempts + 1  # Increases the attempt count

    if guess > secret_number:
        print("Too High")  # Guess is greater than the secret number

    elif guess < secret_number:
        print("Too Low")  # Guess is smaller than the secret number

    else:
        print("Correct!")  # Guess is correct
        print("You guessed it in", attempts, "attempts")
        break  # Stops the game
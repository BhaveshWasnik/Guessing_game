import random

def guessing_game():
    print("Welcome to the Random Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    # Generate a random number
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()

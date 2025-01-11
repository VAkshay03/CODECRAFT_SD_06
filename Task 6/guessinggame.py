import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        # Prompt the user for their guess
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
            break

# Start the game
guessing_game()

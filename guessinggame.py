import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100

    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    guessed_correctly = False

    print(f"I have selected a number between {lower_bound} and {upper_bound}. Can you guess it?")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            elif guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                guessed_correctly = True
                
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Start the game
number_guessing_game() 


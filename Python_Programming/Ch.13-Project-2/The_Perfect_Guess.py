# ===============================================================================================================================
#                                       PROJECT NOTES: THE PERFECT GUESS GAME
# ===============================================================================================================================

# ===============================================================================================================================
# PROJECT DESCRIPTION & REQUIREMENTS
# ===============================================================================================================================

# PROJECT 2 THE PERFECT GUESS
# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays "Lower number please". 
# Similarly, if the user's guess is too low, the program prints "higher number please" When the user guesses the correct number, 
# the program displays the number of guesses the player used to arrive at the number.
# Hint: Use the random module.


# ===============================================================================================================================
# IMPLEMENTATION CODE WITH DETAILED COMMENTS
# ===============================================================================================================================

import random

def perfect_guess():
    """
    Core function to execute 'The Perfect Guess' game.
    It generates a random target number, loops to accept player inputs, 
    provides feedback ('Lower number please' or 'Higher number please'), 
    and tracks total attempts until correct.
    """
    
    # Generate a random number between 1 and 100 (you can adjust the range as needed)
    actual_number = random.randint(1, 100)
    guesses = 0
    
    print("Welcome to The Perfect Guess Game!")
    print("I have generated a random number. Try to guess it!")
    
    # Infinite loop to keep asking the user until they guess correctly
    while True:
        try:
            # Ask the user for their guess and convert input to an integer
            player_guess = int(input("Enter your guess: "))
            
            # Increment the guess counter with every valid attempt
            guesses += 1
            
            # Compare the player's guess with the actual generated number
            if player_guess > actual_number:
                print("Lower number please")
            elif player_guess < actual_number:
                print("Higher number please")
            else:
                # Correct guess reached: display total attempts and exit loop
                print(f"Congratulations! You guessed the correct number in {guesses} guesses.")
                break
                
        except ValueError:
            # Handle invalid non-integer inputs gracefully without crashing the game
            print("Please enter a valid integer.")

# Run the game when executed directly as a script
if __name__ == "__main__":
    perfect_guess()

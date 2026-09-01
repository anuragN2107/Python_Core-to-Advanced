# ==============================================================================
#                 PROJECT 1: SNAKE, WATER, GUN GAME
# ==============================================================================
# We all have played snake, water, gun game in our childhood.
# If you haven't, google the rules of this game and write a python program
# capable of playing this game with the user.
#
# Game Rules:
# 1. Snake (1) drinks Water (-1) -> Snake wins
# 2. Water (-1) douses Gun (0)   -> Water wins
# 3. Gun (0) shoots Snake (1)    -> Gun wins
# ==============================================================================

import random

computer = random.choice([1, -1, 0])

dict_choice = {"snake": 1, "water": -1, "gun": 0}
reverse_dict = {1: "snake", -1: "water", 0: "gun"}

mychoice = int(input("Enter Your Choice (1 for Snake, -1 for Water, 0 for Gun): "))

if mychoice not in reverse_dict:
    print("Invalid Input")
else:
    print(f"You selected : {reverse_dict[mychoice]}\nComputer selected : {reverse_dict[computer]}")

    if (computer == mychoice):
        print("It's a Draw")
    else:
        if (computer == 1 and mychoice == -1):
            print("Sorry! You Lose")
        elif (computer == 1 and mychoice == 0):
            print("Hurray! You Win")
        elif (computer == -1 and mychoice == 1):
            print("Hurray! You Win")
        elif (computer == -1 and mychoice == 0):
            print("Sorry! You Lose")
        elif (computer == 0 and mychoice == 1):
            print("Sorry! You Lose")
        elif (computer == 0 and mychoice == -1):
            print("Hurray! You Win")


# ==============================================================================
# CODE WALKTHROUGH & DOCUMENTATION
# ==============================================================================
#
# 1. CORE MECHANICS & STATE SETUP:
#    - `import random` : Loads Python's built-in module for pseudo-random number generation.
#    - `computer = random.choice([1, -1, 0])`: Randomly selects the computer's choice:
#        *  1 -> Snake
#        * -1 -> Water
#        *  0 -> Gun
#    - `dict_choice` & `reverse_dict`: Map string identifiers to integers and vice versa.
#
# 2. INPUT & VALIDATION:
#    - `mychoice = int(input(...))`: Captures terminal input and converts the string into an integer.
#    - `if mychoice not in reverse_dict:`: Guards against invalid input entries.
#    - `else:`: Proceeds with game resolution if input is valid.
#
# 3. OUTCOME EVALUATION TABLE:
#    +------------------+-----------------------+-------------------+--------------------+
#    | Player (mychoice)| Computer (computer)   | Outcome           | Rule Applied       |
#    +------------------+-----------------------+-------------------+--------------------+
#    | Same choice      | Same choice           | It's a Draw       | Matching values    |
#    | Water (-1)       | Snake (1)             | Sorry! You Lose   | Snake drinks Water |
#    | Gun (0)          | Snake (1)             | Hurray! You Win   | Gun shoots Snake   |
#    | Snake (1)        | Water (-1)            | Hurray! You Win   | Snake drinks Water |
#    | Gun (0)          | Water (-1)            | Sorry! You Lose   | Water douses Gun   |
#    | Snake (1)        | Gun (0)               | Sorry! You Lose   | Gun shoots Snake   |
#    | Water (-1)       | Gun (0)               | Hurray! You Win   | Water douses Gun   |
#    +------------------+-----------------------+-------------------+--------------------+
# ==============================================================================
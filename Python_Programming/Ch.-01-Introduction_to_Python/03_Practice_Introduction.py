# ==============================================================================
# CHAPTER 1: PRACTICE SET (BASIC PYTHON EXERCISES)
# ==============================================================================

# ------------------------------------------------------------------------------
# Question 1:
# Write a Python program to print the poem "Twinkle Twinkle Little Star"
# using a single print statement.
# ------------------------------------------------------------------------------
print("--- Question 1: Poem Output ---")
print('''Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle twinkle little star
How I wonder what you are
Twinkle twinkle little star
Shining brightly and afar
Twinkle star dust all around
From the sky right to the ground
Twinkle twinkle little star
Shining brightly and a far''')


# ------------------------------------------------------------------------------
# Question 2:
# Use the REPL (Interactive Terminal Shell) to calculate the table of 5 up to 4.
# (Outputting programmatically for notes reference)
# ------------------------------------------------------------------------------
print("\n--- Question 2: Table of 5 ---")
print(5 * 1)
print(5 * 2)
print(5 * 3)
print(5 * 4)


# ------------------------------------------------------------------------------
# Question 3:
# Use an external module (pyttsx3) to convert text to speech.
# Note: Requires 'pip install pyttsx3'
# ------------------------------------------------------------------------------
print("\n--- Question 3: Text-to-Speech ---")
import pyttsx3

engine = pyttsx3.init()
engine.say("Twinkle twinkle little star, how I wonder what you are")
engine.runAndWait()


# ------------------------------------------------------------------------------
# Question 4:
# Write a Python program to print the contents of a directory using the os module.
# ------------------------------------------------------------------------------
print("\n--- Question 4: Directory Listing ---")
import os

# Specifies the current directory
directory_path = "."
contents = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for item in contents:
    print(f" - {item}")
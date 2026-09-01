# ==============================================================================
# 1. WHAT IS A MODULE IN PYTHON?
# ==============================================================================
# A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py added.
# Modules allow you to organize code into reusable files.

# Types of Modules:
# 1. Built-in Modules: Pre-installed with Python (e.g., math, os, random, sys).
# 2. External Modules: Third-party modules installed using pip (e.g., numpy, pandas, pyjokes).


# ==============================================================================
# 2. WHAT IS PIP IN PYTHON?
# ==============================================================================
# Pip is the package management system used to install and manage software packages/libraries 
# Written in Python from the Python Package Index (PyPI).
#
# Syntax to install an external package (run in Terminal / Command Prompt):
#   pip install <module_name>
#
# Examples of popular packages:
#   pip install pyjokes
#   pip install numpy
#   pip install pandas
#   pip install matplotlib


# ==============================================================================
# 3. USING AN EXTERNAL MODULE EXAMPLE
# ==============================================================================
# Note: First run 'pip install pyjokes' in your terminal before running this script.

import pyjokes

# Fetch and print a random joke
joke = pyjokes.get_joke()
print("--- Random Joke ---")
print(joke)
print()


# ==============================================================================
# 4. COMMENTS IN PYTHON
# ==============================================================================
# Comments are ignored by the Python interpreter and are used to provide explanations,
# documentation, or notes within the code.

# --- Type 1: Single-Line Comment ---
# This is a single-line comment using the hash symbol (#).
#Example:
# This is a single-line comment

# --- Type 2: Multi-Line Comment / Docstring ---
"""
This is a multi-line comment (or docstring)
enclosed within triple double quotes.
It can span multiple lines cleanly.
"""

'''
This is also a multi-line comment
enclosed within triple single quotes.
'''
#Example:
#This is a multi-line comment
#enclosed within triple double quotes.  
#It can span multiple lines cleanly.

# ==============================================================================
# 5. WHAT IS REPL IN PYTHON?
# ==============================================================================
# REPL stands for Read-Eval-Print Loop.
# It is an interactive programming environment that executes code line by line.
#
# How it works:
# - Read  : Reads the user input (Python expression).
# - Eval  : Evaluates / executes the expression.
# - Print : Prints the resulting output directly to the terminal.
# - Loop  : Loops back and waits for the next input.
#
# How to use REPL:
# 1. Open Terminal / Command Prompt.
# 2. Type 'python' (or 'python3') and hit Enter.
# 3. You will see the prompt '>>>' where you can type code directly.
# 4. Type 'exit()' or press Ctrl+Z (Windows) / Ctrl+D (Mac/Linux) to exit.
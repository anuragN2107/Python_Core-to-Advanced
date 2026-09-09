# ==============================================================================
# 1. WHAT IS PYTHON PROGRAMMING?
# ==============================================================================
# Python is a high-level, interpreted, and general-purpose programming language. 
# It was created by Guido van Rossum and first released in 1991.
# Python's design philosophy emphasizes code readability with its notable use of significant whitespace. 
# It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

# ==============================================================================
# 2. BRIEF HISTORY OF PYTHON
# ==============================================================================
# - 1989: Guido van Rossum began implementation at CWI in the Netherlands as a 
#         successor to the ABC language.
# - Name Origin: Named after the British comedy show "Monty Python's Flying Circus", 
#                not the reptile.
# - 1991: Python 0.9.0 released (introduced classes, exception handling, and functions).
# - 2000: Python 2.0 released (introduced list comprehensions and garbage collection).
# - 2008: Python 3.0 released (major backward-incompatible redesign to fix fundamental flaws).
# - 2020: Python 2 was officially retired (End of Life).

# ==============================================================================
# 3. KEY FEATURES OF PYTHON
# ==============================================================================
# - Simple & Readable: Clean syntax that closely resembles plain English.
# - Interpreted: Code is executed line-by-line, eliminating separate compilation steps.
# - Dynamically Typed: Variable types are determined automatically at runtime.
# - Cross-Platform: Runs on Windows, macOS, Linux, and Unix without code changes.
# - Batteries Included: Comes with a vast standard library and package ecosystem (PyPI).

# ==============================================================================
# 4. BASIC PYTHON BUILDING BLOCKS
# ==============================================================================

# Variables & Dynamic Typing (No type declaration required)
name = "Anurag Srivastva"  # String (str)
age = 25                   # Integer (int)
height = 5.9               # Float (float)
is_learning = True         # Boolean (bool)

# Basic Output
print("Hello Anurag Srivastva! let's get started for Python Programming!")

# Basic Formatted String (f-string)
print(f"User: {name} | Learning Active: {is_learning}")
#Output: User: Anurag Srivastva | Learning Active: True

# ==============================================================================
# 5. HOW TO RUN THIS FILE
# ==============================================================================
# Open your terminal/command prompt, navigate to the folder, and run:
#   python <Filename.py>
# or on some systems:
#   python3 <Filename.py>

#===============================================================================
# 6. PYTHON LANGUAGE FEATURES
#===============================================================================
 #High-Level Language:** Abstracts away hardware/memory management so you write human-readable code.
 #Interpreted:** Executes code line-by-line via the Python Virtual Machine (PVM), allowing fast testing and debugging.
 #Dynamically Typed:** Variable types are detected automatically at runtime without explicit declarations.
 #General-Purpose & Multi-Paradigm:** Supports Procedural, Object-Oriented (OOP), and Functional programming.
 #History:** Created by **Guido van Rossum** in 1989 and released in **1991**. Named after *Monty Python's Flying Circus*.

#===============================================================================
# 7. How Python Code Executes 
#===============================================================================
#Python uses a two-step hybrid execution model:
 #[ Source Code (.py) ] ───> Python Compiler ───> [ Bytecode (.pyc in __pycache__) ] ───> PVM (Interpreter) ───> CPU Execution
# ===============================================================================================================================
#                                       PRACTICE EXERCISES: THE WALRUS OPERATOR (:=)
# ===============================================================================================================================
# This file contains 5 practice questions with intuitive explanations, clear comments, and fully executable code.


# ===============================================================================================================================
# QUESTION 1: Checking String Length in an `if` Statement
# ===============================================================================================================================
# Question: Check the length of "Data Science". If it's greater than 8, display the character count.

text = "Data Science"

# The walrus operator (:=) calculates the length of 'text', stores it in 'n', and immediately checks if 'n' is greater than 8 in a single expression.
if (n := len(text)) > 8:
    print(f"The string is long with {n} characters.")

#Output:
#The string is long with 12 characters.

# ===============================================================================================================================
# QUESTION 2: Accumulating Numbers in a `while` Loop
# ===============================================================================================================================
# Question: Using an iterator [4, 8, 12, 0], add numbers to a total until 0 is encountered.

number_stream = iter([4, 8, 12, 0]) # Creating an iterator to simulate a data stream or user input stream
total_sum = 0

# Inside the while loop condition:
# 1. next(number_stream) grabs the next number.
# 2. (num := ...) assigns it to 'num'.
# 3. != 0 checks if it's not zero. The loop stops automatically when 0 is reached.
while (num := next(number_stream)) != 0:
    total_sum += num

print(f"Total Sum: {total_sum}")

#Output:
#Total Sum: 24


# ===============================================================================================================================
# QUESTION 3: Optimizing a List Comprehension
# ===============================================================================================================================
# Question: For numbers 1 to 6, triple each number using a function and keep those > 10.

def triple(x):
    return x * 3

# Here, the walrus operator computes the tripled value 'y' once per iteration,
# filters out values <= 10, and includes 'y' in the resulting list without calling triple() twice.
filtered_results = [y for x in range(1, 7) if (y := triple(x)) > 10]

print(f"Filtered Tripled Values: {filtered_results}")

#Output:
#Filtered Tripled Values: [12, 15, 18]

# ===============================================================================================================================
# QUESTION 4: Substring Index Searching
# ===============================================================================================================================
# Question: Check if "operators" exists in a sentence using .find() and show its index.

sentence = "Mastering Python decorators and operators"
target = "operators"

# .find() returns the index position, or -1 if the substring is missing.
# The walrus operator assigns this index to 'index' and verifies it is not equal to -1.
if (index := sentence.find(target)) != -1:
    print(f"Found '{target}' at index position: {index}")
else:
    print("Substring not found.")

#Output:
#Found 'operators' at index position: 32

# ===============================================================================================================================
# QUESTION 5: Processing Data Streams / Chunks
# ===============================================================================================================================
# Question: Process chunks from a list iterator until an empty chunk [] stops the loop.

stream = iter([['apple', 'banana'], ['cherry', 'date'], []])  # Stream containing lists of items, ending with an empty list

# The while loop fetches the next chunk, assigns it to 'chunk', and evaluates it.
# In Python, empty lists evaluate to False, which safely stops the loop.
while (chunk := next(stream)):
    print(f"Successfully processed chunk: {chunk}")

print("Stream processing completed.")

#Output:
#Successfully processed chunk: ['apple', 'banana']
#Successfully processed chunk: ['cherry', 'date']
#Stream processing completed.
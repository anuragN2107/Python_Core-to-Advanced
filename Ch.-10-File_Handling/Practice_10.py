# ==========================================
# CHAPTER 9 PRACTICE SET - PYTHON FILE I/O
# ==========================================


# ------------------------------------------
# 1. Read 'poems.txt' and check for 'twinkle'
# ------------------------------------------

# Method 1: Using traditional open() and close()
file = open("poem.txt", "w") 
file.write("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are")
file.close()

file = open("poem.txt", "r")   
content = file.read()
file.close()

if "twinkle" in content.lower():   
    print("The file contain the word 'twinkle'")
else:
    print("The file does not contain the word 'twinkle'")


# Method 2: Using 'with' context manager (Recommended)
with open("poem.txt", "w") as file:
    file.write("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are")

with open("poem.txt", "r") as file:
    content = file.read()

if "twinkle" in content.lower():
    print("The file contains the word 'twinkle'")
else:
    print("The file does not contain the word 'twinkle'")



# ------------------------------------------
# 2. Game high-score tracking program
# ------------------------------------------
import random

# Step 1: Create a function that gives a random score between 1 and 1000
def game():
    return random.randint(1, 1000)

# Step 2: Play the game and save the result in the 'score' variable
score = game()
print(f"You scored: {score}")

# Step 3: Open the file in 'append' ("a") mode to safely create it if missing
with open("Hi-score.txt", "a") as file:  
    pass

# Step 4: Open the file in 'read' ("r") mode to get the saved high score
with open("Hi-score.txt", "r") as file:
    highscore = file.read()

# Step 5: Check if the file is completely empty
if highscore == "":
    with open("Hi-score.txt", "w") as file:
        file.write(str(score))
    print(f"You have set the first high score: {score}")

# Step 6: Check if the new score beats the old high score
elif int(highscore) < score:
    with open("Hi-score.txt", "w") as file:
        file.write(str(score))
    print(f"You have broken the old high score of: {highscore}")

# Step 7: If score is lower or equal
else:
    print(f"You have not broken the high score of: {highscore}")
    


# ------------------------------------------
# 3. Generate multiplication tables (2 to 20)
# ------------------------------------------
for i in range(2, 21):    # Step 1: Pick numbers 2 through 20
    # Step 2: Create a new text file for each table
    with open(f"table_{i}.txt", "w") as file:        
        # Step 3: Multiply each number by 1 through 10
        for j in range(1, 11):            
            # Step 4: Write the equation into the file
            file.write(f"{i} x {j} = {i * j}\n")            

# Step 5: Print completion message
print("All tables from 2 to 20 have been saved in this folder!")



# ------------------------------------------
# 4. Replace "donkey" with "######" in a file
# ------------------------------------------
# Step 1: Define the original story text
content = """The brave donkey walked down the road with another donkey. 
A small donkey met a big donkey, and they both brayed like a happy donkey. 
If you see a donkey, give that donkey a carrot because every donkey loves carrots."""

# Step 2: Create the file and write the text
with open("Donkey.txt", "w") as file:
  file.write(content)

# Step 3: Define search word
word = "donkey"

# Step 4: Read content back from the file
with open("Donkey.txt", "r") as file:
  content = file.read()

# Step 5: Replace instances of the word
new_content = content.replace("donkey", "######")  

# Step 6: Overwrite the file with updated content
with open("Donkey.txt", "w") as file:
  file.write(new_content)



# ------------------------------------------
# 5. Mine a log file for 'python'
# ------------------------------------------
log_data = """[10:00:01] INFO: System boot sequence initiated.
[10:05:22] ERROR: Failed to load config.json.
[10:12:45] INFO: Starting Python backend server.
[10:15:00] WARN: Memory usage high."""

# Create sample log file
with open("log.txt", "w") as file:
    file.write(log_data)

# Read and check log content
with open("log.txt", "r") as file:
    content = file.read()

if "python" in content.lower():
    print("Yes, the word 'python' is in the log file!")
else:
    print("No, the word 'python' was not found.")



# ------------------------------------------
# 6. Find line number where 'python' is present
# ------------------------------------------

# Approach 1: Using a standard for loop
with open("log.txt", "r") as file:
    line_number = 1
    for line in file:
        if "python" in line.lower():
            print(f"The word 'python' is present on line number: {line_number}")
        line_number += 1

# Approach 2: Using readline() and break inside a while loop
with open("log.txt", "r") as file:
    line_number = 1
    line = file.readline()
    
    while line:
        if "python" in line.lower():
            print(f"The word 'python' is present on line number: {line_number}")
            break
        line = file.readline()
        line_number += 1



# ------------------------------------------
# 9. Make a copy of a text file
# ------------------------------------------
content = "He is a king."

with open("this1.txt", "w") as file:
  file.write(content)

with open("this1.txt", "r") as file:
    content = file.read()

with open("this1_copy.txt", "w") as file:
    file.write(content)



# ------------------------------------------
# 10. Check if two files are identical
# ------------------------------------------
with open("file1.txt", "w") as file:
    file.write("Learning Python is fun.\nLet's compare these files.")

with open("file2.txt", "w") as file:
    file.write("Learning Python is fun.\nLet's compare these files.")

with open("file1.txt", "r") as file1:
    content1 = file1.read()

with open("file2.txt", "r") as file2:
    content2 = file2.read()

if content1 == content2:
    print("The files are identical and match perfectly.")
else:
    print("The files are not identical.")



# ------------------------------------------
# 11. Wipe out the content of a file
# ------------------------------------------
with open("wipe_test.txt", "w") as file:
    file.write("This data will be erased shortly.")

# Overwriting with an empty string to wipe it clean
with open("wipe_test.txt", "w") as file:
    file.write("")



# ------------------------------------------
# 12. Rename a file using Python
# ------------------------------------------
import os

with open("old_file.txt", "w") as file:
    file.write("This file is going to be renamed.")

# Rename operation
os.rename("old_file.txt", "renamed_by_python.txt")
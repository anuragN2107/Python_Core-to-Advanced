# # CHAPTER 5-PRACTICE SET

# # 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
# words={
#     "madad":"Help",
#     "kursi":"Chair",
#     "kutta":"Dog",
#     "hathi":"Elephant"
# }
# # words["sher"]="Lion"    #Add elements to the dictionary
# # words["bagh"]="Tiger"
# # words["tendua"], words["ghoda"] = "Leopard", "Horse"

# word=input("Enter the Hindi word:")
# print(words.get(word)) 
# if words.get(word) is None:
#     print("Word not found")

# # 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
# unique_numbers = set()
# for i in range(8):
#     num = int(input(f"Enter number {i + 1}: "))
#     unique_numbers.add(num)
# print("\nUnique numbers entered:", unique_numbers)

#                               #OR
# unique_numbers = {
#     int(input("Enter number 1: ")),
#     int(input("Enter number 2: ")),
#     int(input("Enter number 3: ")),
#     int(input("Enter number 4: ")),
#     int(input("Enter number 5: ")),
#     int(input("Enter number 6: ")),
#     int(input("Enter number 7: ")),
#     int(input("Enter number 8: ")),
# }
# print("\nUnique numbers entered:", unique_numbers)

# # 3. Can we have a set with 18 (int) and "18" (str) as a value in it?
# s=set()
# s.add(18)
# s.add("18")
# print(s) #output: {18} #Yes we can

# # 4. What will be the length of following set S:

# s = set()

# s.add(20)

# s.add(20.0)

# s.add('20') # length of s after these operations?

s1 = set()
s1.add(20)
s1.add(20.0) #Python compares numbers by their mathematical value, implicitly converting the integer 20 to a float (20.0) before evaluating equality.
s1.add('20')
print(s1)
print(len(s1)) #output: 2

# # 5. S={}   What is the type of S? 
#Answer=output: dict

#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
s={}
print(type(s)) #output: dict
s["Ram"]="C"
s["Laxman"]="C++"
s["Bharat"]="Java"
s["Satrughan"]="Python"
print(s) #output: {'Ram': 'C', 'Laxman': 'C++', 'Bharat': 'Java', 'Satrughan': 'Python'}

# # 7. If the names of 2 friends are same; what will happen to the program in problem 6?
s2={}
name=input("Enter your name:") #input: Ram
lang=input("Enter your favourite language:") #input: C
s2.update({name:lang})

name=input("Enter your name:") #input: Ram
lang=input("Enter your favourite language:") #input: Java
s2.update({name:lang})
print(s2) 
#output: Enter your name:Ram
# Enter your favourite language:C++
# Enter your name:Ram
# Enter your favourite language:Java
# {'Ram': 'Java'} #This is because we are updating the dictionary with the same key twice


# # 8. If languages of two friends are same; what will happen to the program in problem 6? #
s2={}
name=input("Enter your name:") #input: Ram
lang=input("Enter your favourite language:") #input: C
s2.update({name:lang})

name=input("Enter your name:") #input: Ram
lang=input("Enter your favourite language:") #input: Java
s2.update({name:lang})
print(s2) 
#Output
# Enter your favourite language:Java
# Enter your name:Shyam
# Enter your favourite language:Java
# {'Ram': 'Java', 'Shyam': 'Java'}
#  #We will get both the key value pairs as we can have same values for different keys.

# # 9. Can you change the values inside a list which is contained in set S?
#  s={ 8,7,12,"Harry",[1,2]}

#Answer:No, because in Python you cannot put a list inside a set in the first place.

#If you try to execute s = {8, 7, 12, "Harry", [1, 2]}, Python immediately raises an error:

#If you want to store a sequence of items inside a set, use an immutable tuple (() instead of []):

# ==============================================================================
#                 CHAPTER 5: PRACTICE SET (SOLUTIONS & NOTES)
# ==============================================================================

# ------------------------------------------------------------------------------
# Problem 1: Create a dictionary of Hindi words with English translations.
#            Provide the user with an option to look it up!
# ------------------------------------------------------------------------------
words = {
    "madad": "Help",
    "kursi": "Chair",
    "kutta": "Dog",
    "hathi": "Elephant"
}

# Optional: Adding extra elements to the dictionary
# words["sher"] = "Lion"
# words["bagh"] = "Tiger"
# words["tendua"], words["ghoda"] = "Leopard", "Horse"

word = input("Enter the Hindi word: ")
result = words.get(word)

if result is not None:
    print(f"English Meaning: {result}")
else:
    print("Word not found")


# ------------------------------------------------------------------------------
# Problem 2: Input eight numbers from the user and display all unique numbers.
# ------------------------------------------------------------------------------
# Approach 1: Using a for loop
unique_numbers = set()
for i in range(8):
    num = int(input(f"Enter number {i + 1}: "))
    unique_numbers.add(num)
print("\nUnique numbers entered:", unique_numbers)

# Approach 2: Using set literal syntax
# unique_numbers = {
#     int(input("Enter number 1: ")),
#     int(input("Enter number 2: ")),
#     int(input("Enter number 3: ")),
#     int(input("Enter number 4: ")),
#     int(input("Enter number 5: ")),
#     int(input("Enter number 6: ")),
#     int(input("Enter number 7: ")),
#     int(input("Enter number 8: ")),
# }
# print("\nUnique numbers entered:", unique_numbers)


# ------------------------------------------------------------------------------
# Problem 3: Can we have a set with 18 (int) and "18" (str) as a value in it?
# ------------------------------------------------------------------------------
s = set()
s.add(18)
s.add("18")
print(s)  # Output: {18, '18'}
# Answer: Yes, we can, because int (18) and str ("18") have different data types and hashes.


# ------------------------------------------------------------------------------
# Problem 4: What will be the length of the following set S?
# ------------------------------------------------------------------------------
s1 = set()
s1.add(20)
s1.add(20.0)  # Python compares numbers by numeric value (20 == 20.0 is True and hash(20) == hash(20.0))
s1.add('20')

print(s1)       # Output: {20, '20'}
print(len(s1))  # Output: 2


# ------------------------------------------------------------------------------
# Problem 5: S = {} — What is the data type of S?
# ------------------------------------------------------------------------------
S = {}
print(type(S))  # Output: <class 'dict'>
# Answer: It is a dictionary (dict). To create an empty set, use `set()`.


# ------------------------------------------------------------------------------
# Problem 6: Create an empty dictionary. Allow 4 friends to enter their favorite
#            language as value and use their names as keys (Unique names).
# ------------------------------------------------------------------------------
friends_fav = {}
print(type(friends_fav))  # Output: <class 'dict'>

friends_fav["Ram"] = "C"
friends_fav["Laxman"] = "C++"
friends_fav["Bharat"] = "Java"
friends_fav["Satrughan"] = "Python"

print(friends_fav)
# Output: {'Ram': 'C', 'Laxman': 'C++', 'Bharat': 'Java', 'Satrughan': 'Python'}


# ------------------------------------------------------------------------------
# Problem 7: If the names of 2 friends are the same, what will happen?
# ------------------------------------------------------------------------------
s2 = {}

name = input("Enter your name: ")                     # Input: Ram
lang = input("Enter your favourite language: ")       # Input: C
s2.update({name: lang})

name = input("Enter your name: ")                     # Input: Ram
lang = input("Enter your favourite language: ")       # Input: Java
s2.update({name: lang})

print(s2)
# Output: {'Ram': 'Java'}
# Explanation: Dictionary keys must be unique. The second entry overwrites the value of the first.


# ------------------------------------------------------------------------------
# Problem 8: If the languages of 2 friends are the same, what will happen?
# ------------------------------------------------------------------------------
s3 = {}

name = input("Enter your name: ")                     # Input: Ram
lang = input("Enter your favourite language: ")       # Input: Java
s3.update({name: lang})

name = input("Enter your name: ")                     # Input: Shyam
lang = input("Enter your favourite language: ")       # Input: Java
s3.update({name: lang})

print(s3)
# Output: {'Ram': 'Java', 'Shyam': 'Java'}
# Explanation: Both key-value pairs are preserved because dictionary values do not have to be unique.


# ------------------------------------------------------------------------------
# Problem 9: Can you change the values inside a list which is contained in set S?
#            s = {8, 7, 12, "Harry", [1, 2]}
# ------------------------------------------------------------------------------
# Answer:
# No, because in Python you cannot put a list inside a set in the first place.
#
# Attempting to execute `s = {8, 7, 12, "Harry", [1, 2]}` immediately raises:
# TypeError: unhashable type: 'list'
#
# If you want to store an immutable sequence inside a set, use a tuple `()`:
# valid_set = {8, 7, 12, "Harry", (1, 2)}
# ==============================================================================
# ===========================================================================================
# CHAPTER 11 PRACTICE SET - OBJECT ORIENTED PROGRAMMING
# =========================================================================================

# -------------------------------------------------------------------------------------------
# 1. Create a Class "Programmer" to store information of programmers working at Microsoft.
# --------------------------------------------------------------------------------------------

class Programmer:
    # Class attribute shared by all instances (company name)
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        # Instance attributes specific to each programmer
        self.name = name
        self.salary = salary
        self.pin = pin

# Creating objects (instances) for different programmers
p1 = Programmer("Alice", 120000, 560001)
p2 = Programmer("Bob", 150000, 560002)

# Printing programmer details
print(p1.company, p1.name, p1.salary, p1.pin)
print(p2.company, p2.name, p2.salary, p2.pin)


# -------------------------------------------------------------------------------------------
# 2. Write a class "Calculator" capable of finding square, cube, and square root of a number.
# -------------------------------------------------------------------------------------------

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def __init__(self, n):
        # Store the input number as an instance attribute
        self.n = n

    def square(self):
        # Calculate and return the square of the number
        return self.n ** 2

    def cube(self):
        # Calculate and return the cube of the number
        return self.n ** 3

    def sqrt(self):
        # Calculate and return the square root of the number
        return self.n ** 0.5


# Prompt the user for input, convert it to an integer, and instantiate the class
calc = Calculator(int(input("Enter a number: ")))

# Call each method using parentheses () and access the stored number via calc.n
print(f"Square of {calc.n}:- {calc.square()}")
print(f"Cube of {calc.n}:- {calc.cube()}")
print(f"Square root of {calc.n}:- {calc.sqrt()}")


# -------------------------------------------------------------------------------------------
# 3. Create a class with a class attribute 'a', set 'a' using object.a, and check if it changes the class attribute.
# -------------------------------------------------------------------------------------------

class Sample:
    a = 10  # Class attribute

obj = Sample()
obj.a = 0  # Creating an instance attribute 'a' for this specific object (does not modify class attribute)

print("Instance attribute value:", obj.a)      # Accesses instance attribute
print("Class attribute value:", Sample.a)   # Accesses original class attribute

# Explanation: No, setting object.a = 0 creates a new instance attribute for that specific object and shadows the class attribute.
# The class attribute Sample.a remains unchanged at 10.


# -------------------------------------------------------------------------------------------
# 4. Add a static method in problem 2, to greet the user with hello.
# -------------------------------------------------------------------------------------------

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""
    def __init__(self, n):
        # Store the input number as an instance attribute
        self.n = n
    
    def square(self):
        # Calculate and return the square of the number
        return self.n ** 2
    
    def cube(self):
        # Calculate and return the cube of the number
        return self.n ** 3
    
    def sqrt(self):
        # Calculate and return the square root of the number
        return self.n ** 0.5
    
    @staticmethod
    def greet():
        print("Hello!")

calc = Calculator(int(input("Enter a number: ")))
calc.greet()


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
# ----------------------------------------------------------------------------------------------------------------------------------------------------
class Train:  # Define a class named Train to manage train details, fares, and bookings

  # The constructor method initializes the object's attributes when created
  def __init__(self, name, fare, seats):
    self.name = name  # Store the name of the train
    self.fare = fare  # Store the ticket price
    self.seats = seats  # Store the number of available seats

  # Method to check and display the current train status and available seats
  def get_status(self):
    print(f"--- Train Status: {self.name} ---")
    print(f"Available Seats: {self.seats}")

  # Method to display the ticket fare information
  def get_fare_info(self):
    print(f"The fare for {self.name} is INR {self.fare}")

  # Method to handle ticket bookings and update available seats
  def book_ticket(self):
    # Check if there is at least one seat available
    if self.seats > 0:
      print(f"Ticket booked successfully! Assigned seat: {self.seats}")
      self.seats -= 1  # Reduce the available seat count by 1 after booking
    else:
      print("Sorry, this train is fully booked!")


# --- Execution Phase ---

# Create an instance of the Train class named 'intercity'
intercity = Train("Rajdhani Express", 1500, 3)

# Check the initial status of the train (shows 3 available seats)
intercity.get_status()

# Display the fare information for the train
intercity.get_fare_info()

# Book a ticket, which triggers the condition and decreases the seat count from 3 to 2
intercity.book_ticket()

# Check the updated status of the train to verify the seat reduction
intercity.get_status()


# -------------------------------------------------------------------------------------------
# 6. Can you change the self-parameter inside a class to something else (say "harry")?
# -------------------------------------------------------------------------------------------

class Sample:
    def __init__(harry, name):
        # 'harry' works identically to 'self' (it's just a variable name for the object reference)
        harry.name = name

    def print_name(sif):
        # 'sif' acts as the object reference parameter here
        print(sif.name)

obj = Sample("Python")
obj.print_name()

# Explanation: Yes, you can change the self-parameter to any valid variable name (like "harry" or "sif"). However, it is a strong convention in Python to use 'self' for clarity and consistency. Changing it may confuse other developers reading your code.
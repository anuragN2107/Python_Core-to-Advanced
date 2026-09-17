# ===============================================================================================================================
#                               PYTHON ABSTRACTION: PRACTICE SET 
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 1: Creating an Abstract Base Class
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Import the `ABC` class and `abstractmethod` decorator from the `abc` module, and define an abstract class `Machine`.
print("--- Question 1: Defining an Abstract Base Class ---")

from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def power_on(self):
        """Abstract method: Forces all child classes to provide an implementation."""
        pass

print("Abstract base class 'Machine' created successfully.")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 2: Implementing a Child Class
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a child class `Computer` that inherits from `Machine` and implements the `power_on` method.
print("\n--- Question 2: Implementing Child Class ---")

class Computer(Machine):
    def power_on(self):
        # Implementing the mandatory abstract method from the parent class
        print("Computer booting up... Loading operating system.")

comp = Computer()
comp.power_on()


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 3: Preventing Direct Instantiation
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Show that attempting to create an object directly from an abstract class (`Machine`) raises a `TypeError`.
print("\n--- Question 3: Preventing Direct Instantiation ---")

try:
    # Abstract classes cannot be instantiated directly
    invalid_machine = Machine()
except TypeError as err:
    print(f"[Caught Expected Error]: {err}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 4: Combining Abstract and Concrete Methods
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create an abstract class `Worker` with an abstract method `work()` and a concrete (regular) method `take_break()`.
print("\n--- Question 4: Abstract and Concrete Methods Together ---")

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    def take_break(self):
        # Concrete method with default shared logic for all workers
        print("Taking a 15-minute coffee break.")

class Chef(Worker):
    def work(self):
        print("Chef is cooking meals in the kitchen.")

chef = Chef()
chef.work()         # Calls the implemented abstract method
chef.take_break()   # Calls the inherited concrete method


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 5: Multiple Subclass Implementations
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create an abstract class `Payment` with an abstract method `pay(amount)`, and two child classes `CreditCard` and `PayPal`.
print("\n--- Question 5: Multiple Subclass Implementations ---")

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal account.")

gateways = [CreditCard(), PayPal()]
for gateway in gateways:
    gateway.pay(100.00)


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 6: Enforcing Implementation (Missing Method Error)
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a child class from an abstract base class without implementing the abstract method, and catch the resulting error.
print("\n--- Question 6: Enforcing Implementation ---")

class Appliance(ABC):
    @abstractmethod
    def run(self):
        pass

class Fan(Appliance):
    pass  # Forgot to implement the 'run' method!

try:
    f = Fan()  # Raises TypeError because 'run' was not overridden
except TypeError as e:
    print(f"[Enforced Error Caught]: {e}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 7: Abstract Properties
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create an abstract class `Database` that requires any child class to implement an abstract property called `connection_string`.
print("\n--- Question 7: Abstract Properties ---")

class Database(ABC):
    @property
    @abstractmethod
    def connection_string(self):
        pass

class MongoDatabase(Database):
    @property
    def connection_string(self):
        return "mongodb://localhost:27017"

db = MongoDatabase()
print(f"Connection String: {db.connection_string}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 8: Comprehensive Abstraction Architecture
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Build an abstract class `RemoteControl` with an abstract method `press_button()`, and implement a `TVRemote` subclass.
print("\n--- Question 8: Comprehensive Abstraction Example ---")

class RemoteControl(ABC):
    @abstractmethod
    def press_button(self):
        pass

    def description(self):
        print("This is a universal remote control layout.")

class TVRemote(RemoteControl):
    def press_button(self):
        print("TV Remote: Power button pressed. TV turned on.")

tv_remote = TVRemote()
tv_remote.description()  # Using shared concrete method
tv_remote.press_button() # Using enforced abstract method
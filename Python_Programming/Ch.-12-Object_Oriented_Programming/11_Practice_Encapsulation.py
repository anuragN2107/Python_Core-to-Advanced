# ===============================================================================================================================
#                               PYTHON ENCAPSULATION:  PRACTICE SET 
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 1: Public Attributes and Methods
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `Car` with public attributes `brand` and `model`, and a public method `get_info()` that returns them.
print("--- Question 1: Public Attributes ---")

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute (accessible anywhere)
        self.model = model  # Public attribute

    def get_info(self):
        return f"Car: {self.brand} {self.model}"

my_car = Car("Toyota", "Camry")
print(my_car.get_info())
print(my_car.brand)  # Directly accessible outside the class


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 2 : Protected Attributes (Single Underscore Convention)
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `Employee` with a protected attribute `_department`. Show that it can be accessed, but signals internal use.
print("\n--- Question 2: Protected Attributes ---")

class Employee:
    def __init__(self, name, department):
        self.name = name
        self._department = department  # Protected convention (warning: internal use only)

emp = Employee("Alice", "Engineering")
print(f"Name: {emp.name}")
print(f"Department (Protected): {emp._department}")  # Python allows it, but it's discouraged


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 3 : Private Attributes (Data Hiding)
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `BankAccount` with a private attribute `__pin`. Show that attempting to access it directly throws an error.
print("\n--- Question 3: Private Attributes & Data Hiding ---")

class BankAccount:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin  # Private attribute (hidden using double underscore)

acc = BankAccount("Bob", 1234)
try:
    print(acc.__pin)  # This will raise an AttributeError
except AttributeError as e:
    print(f"[Blocked]: Cannot access private attribute directly -> {e}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 4 : Getter Property for Private Data
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Using the `BankAccount` class, add a `@property` getter so users can safely read the private `__pin` value.
print("\n--- Question 4: Getter Property ---")

class SecureAccount:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin

    @property
    def pin(self):
        """Getter: Safely exposes private __pin for reading."""
        return self.__pin

secure_acc = SecureAccount("Charlie", 5678)
print(f"Accessed safely via Getter property: {secure_acc.pin}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 5 (Advanced): Setter Property with Validation Logic
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `UserScore` with a private `__score`. Add a setter that ensures the score can never be set below 0.
print("\n--- Question 5: Setter Validation Logic ---")

class UserScore:
    def __init__(self, score):
        self.score = score  # Triggers setter on initialization

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        """Setter: Validates input before modifying private data."""
        if value < 0:
            print("[Validation Error]: Score cannot be negative! Defaulting to 0.")
            self.__score = 0
        else:
            self.__score = value

player = UserScore(50)
print(f"Initial Score: {player.score}")
player.score = -20  # Triggers validation rule
print(f"Score after invalid update: {player.score}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 6 : Read-Only Property (Getter without Setter)
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `DatabaseConfig` with a private `__host` variable. Provide a getter so it can be read, but no setter.
print("\n--- Question 6: Read-Only Property ---")

class DatabaseConfig:
    def __init__(self, host):
        self.__host = host

    @property
    def host(self):
        """Read-only property because no setter is defined."""
        return self.__host

config = DatabaseConfig("localhost")
print(f"Host (Read-Only): {config.host}")

try:
    config.host = "remotehost"  # Raises AttributeError because there is no setter
except AttributeError as e:
    print(f"[Blocked Modification]: {e}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 7 : Demonstration of Name Mangling
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Explain and demonstrate how Python's name mangling renames `__secret` internally to `_ClassName__secret`.
print("\n--- Question 7: Name Mangling Demonstration ---")

class Agent:
    def __init__(self, code):
        self.__secret_code = code  # Python renames this to _Agent__secret_code internally

agent_obj = Agent("Omega-7")

# Accessing via the mangled name generated by Python
print("Accessed via Name Mangling lookup:", agent_obj._Agent__secret_code)


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 8 : Comprehensive Encapsulation System
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Build a `Product` class combining private attributes (`__price`, `__stock`), getters, and setters with strict checks.
print("\n--- Question 8: Comprehensive Encapsulation System ---")

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price    # Uses price setter
        self.stock = stock    # Uses stock setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero.")
        self.__price = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            self.__stock = 0
        else:
            self.__stock = value

# Testing the comprehensive product encapsulation
item = Product("Laptop", 999.99, 10)
print(f"Product: {item.name}, Price: ${item.price}, Stock: {item.stock}")

item.stock = 15  # Valid update via setter
print(f"Updated Stock: {item.stock}")
# ===============================================================================================================================
#                                       PYTHON ENCAPSULATION: MASTER GUIDE & NOTES
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# WHAT IS ENCAPSULATION? (CORE DEFINITION)
# -------------------------------------------------------------------------------------------------------------------------------
# Encapsulation is one of the core fundamental principles of Object-Oriented Programming (OOP). 
# It refers to the bundling of data (attributes) and methods that operate on that data into a single unit (a class), 
# and restricting direct access to some of an object's components.
#
# Why Use Encapsulation?
# 1. Data Hiding / Security: Prevents accidental modification or corruption of sensitive data from outside the class.
# 2. Control: Allows developers to control how data is viewed or updated through controlled interfaces (Getters and Setters).
# 3. Maintainability: Changes can be made to the internal implementation of a class without breaking external code.
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# ACCESS MODIFIERS IN PYTHON
# ===============================================================================================================================
# Unlike languages like Java or C++, Python does not have strict private/protected keywords. 
# Instead, it uses naming conventions with underscores to signal the intended visibility level:
#
# 1. Public Members (No Underscore): 
#    - Can be accessed and modified freely from anywhere inside or outside the class.
# 
# 2. Protected Members (Single Underscore `_`): 
#    - Signaled by a single leading underscore (e.g., `self._age`). 
#    - It is a convention/warning to programmers meaning "do not access this outside the class unless you are in a subclass." 
#    - Python still allows direct access, but it flags intent.
#
# 3. Private Members (Double Underscore `__`): 
#    - Signaled by a double leading underscore (e.g., `self.__balance`).
#    - Triggers **Name Mangling** in Python: Python automatically changes the internal name of the attribute to `_ClassName__variable` 
#      to prevent accidental access from outside.
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# PRACTICAL CODE EXAMPLE: ACCESS MODIFIERS & GETTERS/SETTERS
# ===============================================================================================================================

print("=== ENCAPSULATION DEMONSTRATION ===")

class BankAccount:
    def __init__(self, owner, balance):
        # Public attribute
        self.owner = owner
        
        # Protected attribute (Convention: internal use only)
        self._account_type = "Savings"
        
        # Private attribute (Name mangled: securely hidden)
        self.__balance = balance

    # --- 1. PUBLIC METHOD (Accessible anywhere) ---
    def get_account_summary(self):
        return f"Owner: {self.owner}, Type: {self._account_type}"

    # --- 2. GETTER METHOD (@property) for Private Data ---
    @property
    def balance(self):
        """Safely exposes the private __balance attribute for reading."""
        return self.__balance

    # --- 3. SETTER METHOD (@balance.setter) with Validation ---
    @balance.setter
    def balance(self, amount):
        """Safely controls modifications to the private __balance attribute."""
        if amount < 0:
            print("[Security Error]: Balance cannot be negative!")
        else:
            self.__balance = amount


# =====================================================================
# TESTING ENCAPSULATION AND ACCESS LEVELS
# =====================================================================

acc = BankAccount("Alice", 5000)

# 1. Accessing Public Member (Allowed)
print(f"Owner (Public): {acc.owner}")

# 2. Accessing Protected Member (Allowed by Python, but discouraged by convention)
print(f"Account Type (Protected): {acc._account_type}")

# 3. Attempting to access Private Member directly (Will raise an AttributeError!)
try:
    print(acc.__balance)
except AttributeError as e:
    print(f"Direct Private Access Blocked: {e}")

# 4. Accessing Private Data Safely via the Getter Property
print(f"Balance via Getter Property: ${acc.balance}")

# 5. Modifying Private Data Safely via the Setter Property with Validation
acc.balance = 7500  # Valid update
print(f"Updated Balance: ${acc.balance}")

acc.balance = -2000  # Triggers security validation error
print(f"Balance after invalid attempt: ${acc.balance}")
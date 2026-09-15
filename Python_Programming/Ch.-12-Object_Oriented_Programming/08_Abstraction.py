# ===============================================================================================================================
#                                       PYTHON ABSTRACTION: MASTER GUIDE & NOTES
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# WHAT IS ABSTRACTION? (CORE DEFINITION)
# -------------------------------------------------------------------------------------------------------------------------------
# Abstraction is one of the four core principles of Object-Oriented Programming (OOP), alongside Inheritance, Polymorphism, and Encapsulation.
# 
# Definition:
# Abstraction is the process of **hiding complex implementation details** and showing only the essential features of an object. 
# Think of driving a car: you press the accelerator to move forward, but you don't need to know how the fuel injectors, spark plugs, 
# or engine pistons work under the hood. The complexity is abstracted away from you.
#
# Why Use Abstraction?
# 1. Reduces Complexity: Focuses on *what* an object does rather than *how* it does it.
# 2. Enforces Consistency: Acts as a strict blueprint or template for child classes to follow.
# 3. Prevents Direct Instantiation: Abstract classes cannot be used to create objects directly; they exist only to be inherited.
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# HOW PYTHON IMPLEMENTS ABSTRACTION
# ===============================================================================================================================
# Python does not have a built-in `abstract` keyword like Java or C++. 
# Instead, Python provides a built-in module called `abc` (Abstract Base Classes) to handle abstraction.
#
# Key Components:
# 1. `ABC`: A helper class provided by the `abc` module that turns a normal class into an Abstract Base Class.
# 2. `@abstractmethod`: A decorator used to declare methods that *must* be overridden by any child class. 
#    If a child class fails to implement an abstract method, Python will raise a TypeError.
#
# Syntax Template:
#   from abc import ABC, abstractmethod
#
#   class AbstractParent(ABC):
#       @abstractmethod
#       def my_method(self):
#           pass  # No body in abstract methods
#
#   class Child(AbstractParent):
#       def my_method(self):
#           # Must provide implementation here!
#           print("Implemented!")
# -------------------------------------------------------------------------------------------------------------------------------


# ===============================================================================================================================
# PRACTICAL CODE EXAMPLE: PAYMENT PROCESSOR SYSTEM
# ===============================================================================================================================

print("=== ABSTRACTION DEMONSTRATION ===")

from abc import ABC, abstractmethod

# 1. Abstract Base Class
class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        """
        Abstract Method: Every payment method MUST implement its own version 
        of this logic. It contains no body here.
        """
        pass

    # Concrete method (Abstract classes can also have normal, shared methods)
    def print_receipt(self, amount):
        print(f"[Receipt]: Successfully processed amount of ${amount:.2f}")


# 2. Concrete Child Class 1
class CreditCardPayment(PaymentProcessor):
    
    # Implementing the mandatory abstract method
    def process_payment(self, amount):
        print(f"Connecting to Credit Card Gateway... Charged ${amount:.2f}")


# 3. Concrete Child Class 2
class PayPalPayment(PaymentProcessor):
    
    # Implementing the mandatory abstract method
    def process_payment(self, amount):
        print(f"Redirecting to PayPal Login... Paid ${amount:.2f}")


# =====================================================================
# TESTING ABSTRACTION RULES
# =====================================================================

# Rule 1: You CANNOT instantiate an Abstract Base Class directly!
try:
    invalid_processor = PaymentProcessor()  # Raises TypeError
except TypeError as e:
    print(f"Instantiation Blocked: {e}\n")


# Rule 2: Using the valid concrete child classes that implement the blueprint
print("--- Processing Credit Card ---")
cc_payment = CreditCardPayment()
cc_payment.process_payment(150.00)
cc_payment.print_receipt(150.00)  # Inherited concrete method


print("\n--- Processing PayPal ---")
paypal_payment = PayPalPayment()
paypal_payment.process_payment(75.50)
paypal_payment.print_receipt(75.50)  # Inherited concrete method
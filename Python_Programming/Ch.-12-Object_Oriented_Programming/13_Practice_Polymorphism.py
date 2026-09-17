# ===============================================================================================================================
#                               PYTHON POLYMORPHISM: MASTER PRACTICE SET (Q1 - Q11)
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 1: Method Overriding via Inheritance
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a parent class `Animal` with a method `sound()` and two child classes `Dog` and `Cat` that override it.
print("--- Question 1: Method Overriding ---")

class Animal:
    def sound(self):
        print("Some generic sound...")

class Dog(Animal):
    def sound(self):  # Overrides parent method
        print("Bark! Woof!")

class Cat(Animal):
    def sound(self):  # Overrides parent method
        print("Meow!")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()  # Polymorphic call


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 2: Polymorphic Function Execution
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a function `make_sound(obj)` that accepts any object and calls its `sound()` method.
print("\n--- Question 2: Polymorphic Function ---")

def make_sound(obj):
    obj.sound()  # Executes the specific method based on passed object

make_sound(Dog())
make_sound(Cat())


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 3: Duck Typing Polymorphism
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create two unrelated classes, `PDFReader` and `TextReader`, both having a `read()` method. Use a function to call `read()`.
print("\n--- Question 3: Duck Typing ---")

class PDFReader:
    def read(self):
        print("Reading PDF file contents...")

class TextReader:
    def read(self):
        print("Reading Text file contents...")

def start_reading(reader):
    reader.read()  # Relies on method existence, not class inheritance

start_reading(PDFReader())
start_reading(TextReader())


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 4: Operator Overloading (+)
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `Point` and overload the `+` operator using `__add__` to add coordinates of two points together.
print("\n--- Question 4: Operator Overloading (+) ---")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Triggers p1.__add__(p2)


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 5: Built-in Function Polymorphism (len())
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `Team` that stores a list of players and overloads the `__len__` method to return the team size.
print("\n--- Question 5: Built-in Function Polymorphism (len()) ---")

class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)

team = Team(["Alice", "Bob", "Charlie"])
print(f"Team size: {len(team)}")  # Calls the custom __len__ method


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 6: Extending Behavior with super()
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a base class `Employee` with a work description and a subclass `Manager` that overrides it while using `super()`.
print("\n--- Question 6: Overriding with super() ---")

class Employee:
    def work(self):
        print("Doing general office tasks.")

class Manager(Employee):
    def work(self):
        super().work()  # Calls parent behavior first
        print("Managing the team and reviewing reports.")

mgr = Manager()
mgr.work()


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 7: Polymorphic Salary Calculation
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a base class `Staff` and two subclasses `FullTime` and `Intern`, each implementing a `calculate_pay()` method.
print("\n--- Question 7: Polymorphic Calculation ---")

class Staff:
    def calculate_pay(self):
        return 0

class FullTime(Staff):
    def calculate_pay(self):
        return 4000

class Intern(Staff):
    def calculate_pay(self):
        return 1000

staff_members = [FullTime(), Intern()]
for s in staff_members:
    print(f"Monthly Pay: ${s.calculate_pay()}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 8: Duck Typing with Unrelated Music Instruments
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create classes `Guitar` and `Piano` with a `play()` method, and write a function that plays any instrument passed to it.
print("\n--- Question 8: Unrelated Duck Typing ---")

class Guitar:
    def play(self):
        print("Strumming guitar strings: Strum... strum...")

class Piano:
    def play(self):
        print("Pressing piano keys: Plink... plonk...")

def concert(instrument):
    instrument.play()

concert(Guitar())
concert(Piano())


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 9: Equality Operator Overloading (==)
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `Box` and overload the `==` operator using `__eq__` to compare their volumes.
print("\n--- Question 9: Equality Operator Overloading ---")

class Box:
    def __init__(self, volume):
        self.volume = volume

    def __eq__(self, other):
        return self.volume == other.volume

b1 = Box(50)
b2 = Box(50)
b3 = Box(100)
print(f"Are b1 and b2 equal? {b1 == b2}")
print(f"Are b1 and b3 equal? {b1 == b3}")


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 10: String Representation Overloading (str())
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a class `Book` and overload the `__str__` method to return a custom formatted description string.
print("\n--- Question 10: String Conversion Overloading ---")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' written by {self.author}"

my_book = Book("Python OOP Master Guide", "Expert Dev")
print(my_book)  # Automatically calls __str__


# -------------------------------------------------------------------------------------------------------------------------------
# QUESTION 11: Comprehensive Polymorphism System
# -------------------------------------------------------------------------------------------------------------------------------
# Question: Create a unified rendering system using a parent class `Renderer` and subclasses `HTMLRenderer` and `JSONRenderer`.
print("\n--- Question 11: Comprehensive Polymorphism ---")

class Renderer:
    def render(self, data):
        pass

class HTMLRenderer(Renderer):
    def render(self, data):
        print(f"Rendering data as HTML tags: <p>{data}</p>")

class JSONRenderer(Renderer):
    def render(self, data):
        print(f"Rendering data as JSON format: {{'data': '{data}'}}")

renderers = [HTMLRenderer(), JSONRenderer()]
for rnd in renderers:
    rnd.render("System Active")


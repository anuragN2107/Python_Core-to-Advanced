# ===============================================================================================================================
#                                       CHAPTER 12 PRACTICE SET: Inheritance
# ===============================================================================================================================


# -------------------------------------------------------------------------------------------------------------------------------
# Q1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
# -------------------------------------------------------------------------------------------------------------------------------
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"{self.i}i + {self.j}j"


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)  # Inheriting i and j from the 2-D vector class
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


print("--- Q1 Output ---")
v2 = TwoDVector(1, 2)
v3 = ThreeDVector(1, 2, 3)
print("2D Vector:", v2)
print("3D Vector:", v3)


# -------------------------------------------------------------------------------------------------------------------------------
# Q2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.
# -------------------------------------------------------------------------------------------------------------------------------
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("Dog says: Bow Wow!")


print("\n--- Q2 Output ---")
d = Dog()
d.bark()


# -------------------------------------------------------------------------------------------------------------------------------
# Q3. Create a class 'Employee' and add salary and increment properties to it.
# Write a method 'salaryAfterIncrement' with a @property decorator and a setter which changes the increment based on the salary.
# -------------------------------------------------------------------------------------------------------------------------------
class Employee:
    salary = 4000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Dynamically updates the increment ratio based on the target salary
        self.increment = new_salary / self.salary


print("\n--- Q3 Output ---")
e = Employee()
print("Salary after default increment:", e.salaryAfterIncrement)
e.salaryAfterIncrement = 6000  # Updates increment via setter
print("Updated Increment Value:", e.increment)


# -------------------------------------------------------------------------------------------------------------------------------
# Q4. Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which add and multiply them.
# -------------------------------------------------------------------------------------------------------------------------------
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, other):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


print("\n--- Q4 Output ---")
c1 = Complex(1, 4)
c2 = Complex(2, 3)
print("Addition (c1 + c2):", c1 + c2)
print("Multiplication (c1 * c2):", c1 * c2)


# -------------------------------------------------------------------------------------------------------------------------------
# Q5. Write a class vector representing a vector of n dimensions. Overload the + and * operators for sum and dot product.
# Q6. Write __str__() method to print the vector as follows: 7i + 8j + 10k (Assume dimension 3 for this problem).
# Q7. Override the len() method on vector of problem 5 to display the dimension of the vector.
# -------------------------------------------------------------------------------------------------------------------------------
class Vector:
    def __init__(self, elements):
        self.elements = elements  # Storing n-dimensional components in a list

    def __add__(self, other):
        # Adds corresponding components of two vectors together
        return Vector([a + b for a, b in zip(self.elements, other.elements)])

    def __mul__(self, other):
        # Calculates the dot product (sum of products of corresponding components)
        return sum([a * b for a, b in zip(self.elements, other.elements)])

    def __str__(self):
        # Formats output as 7i + 8j + 10k if dimension is 3
        if len(self.elements) == 3:
            return f"{self.elements[0]}i + {self.elements[1]}j + {self.elements[2]}k"
        return ", ".join(map(str, self.elements))

    def __len__(self):
        # Returns the total dimension count of the vector
        return len(self.elements)


print("\n--- Q5, Q6, Q7 Output ---")
v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

print("Vector 1 string format (__str__):", v1)
print("Vector Sum (v1 + v2):", v1 + v2)
print("Vector Dot Product (v1 * v2):", v1 * v2)
print("Dimension of Vector 1 (__len__):", len(v1))
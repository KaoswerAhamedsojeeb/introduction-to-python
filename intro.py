# Python Basics: Syntax, Data Types, and Control Statements

# Single-line comment
''' Multi-line comment:
This script demonstrates the basic syntax, data types,
and control statements in Python. '''

# Variables and Data Types
integer_var = 10  # Integer
float_var = 20.5  # Float
string_var = "Hello, Python!"  # String
boolean_var = True  # Boolean
list_var = [1, 2, 3, 4, 5]  # List
tuple_var = (10, 20, 30)  # Tuple
dict_var = {"name": "John", "age": 25}  # Dictionary
set_var = {1, 2, 3, 4, 5}  # Set

# Printing variables
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)
print("List:", list_var)
print("Tuple:", tuple_var)
print("Dictionary:", dict_var)
print("Set:", set_var)

# Conditional Statements
num = 15
if num > 10:
    print("Number is greater than 10")
elif num == 10:
    print("Number is 10")
else:
    print("Number is less than 10")

# Loops

# For loop
print("For loop: ", end="")
for i in range(5):  # Loop from 0 to 4
    print(i, end=" ")
print()

# While loop
print("While loop: ", end="")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# Functions
def greet(name):
    """Function to print a greeting message"""
    return f"Hello, {name}!"

# Calling the function
print(greet("Kaoswer"))


# List Comprehension
squares = [x ** 2 for x in range(5)]
print("List Comprehension Squares:", squares)

# Dictionary Iteration
print("Dictionary Iteration:")
for key, value in dict_var.items():
    print(f"{key}: {value}")

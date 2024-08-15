# The Zen of Python
# Importing "this" module will print the Zen of Python, a collection of software principles for writing computer programs.
import this
from typing import List, Dict, Callable

# type hints use them, default to 0
# Function to add two numbers with default values of 0
def add_number(a_pram: int = 0, b_pram: int = 0) -> int:
    return a_pram + b_pram

# Call the add_number function with arguments 4 and 6, store the result in _new_number
new_number: int = add_number(4, 6)
print(f"new number is {new_number}")

im_a_str : str = "I'm a string"
print(f"str value is {im_a_str}")

# Declare an integer variable and print its value
im_a_int: int = 42
print(f"int value is {im_a_int}")

# Declare a float variable and print its value
im_a_float: float = 4.333
print(f"float value is {im_a_float}")

# Check if converting the float to an int results in 4, store the result in _is_it_int
is_it_int: bool = int(im_a_float) == 4
print(f"is it a int? {is_it_int}")

# Check if converting the int to a float results in 42.0, store the result in _is_it_float
is_it_float: bool = float(im_a_int) == 42.0
print(f"is it a float? {is_it_float}")

# Print a formatted string using the format method
print("Nice to meet you {0}. I am {1}".format("Denis", "Computer"))

# Declare a boolean variable
really: bool = True

# Conditional statement to check the value of _really
if really:
    print("really is True!")
else:
    print("really is False")

# Conditional statement with a logical AND
if really and False:
    print("they both have to be True")
else:
    print("the second clause was False")

# Use a ternary operator to check if _a is greater than _b
a: int = 1
b: int = 2
is_it: str = "bigger" if a > b else "smaller"

print(f"is it {is_it}")

# Declare a list of student names
student_names: list[str] = ["mark", "test", "computer"]

# Access and print the first and third elements of the list
print(student_names[0])
print(student_names[2])

# Append a new name to the list
student_names.append("homer")

# Check if "mark" is in the list
if "mark" in student_names:
    print("mark in list")
else:
    print("mark isn't in list")

# Print the length of the list
print(len(student_names))

# Create a new list excluding the first element ("mark")
everyone_but_mark: list[str] = student_names[1:]

# Create a sublist of _everyone_but_mark excluding the first and last elements
list_of_computer: list[str] = everyone_but_mark[1:-1]

# Delete the second element of the list
del student_names[1]

# Print the length of the list after deletion
print(len(student_names))

# Print the sub lists
print(everyone_but_mark)
print(list_of_computer)

# Iterate over the list using a normal for loop
print("Normal for loop")
for name in student_names:
    print(name)

# Iterate over the list using an index-based for loop
print("index for loop")
for index in range(len(student_names)):
    print(student_names[index])

# Iterate over the list and break the loop if "computer" is found
for name in student_names:
    if name == "computer":
        print("Found Computer!")
        break
    print(f"Not computer, it's {name}")

# Initialize a variable and use a while loop to count up to 20
x: int = 10
while x < 20:
    print(f"count at {x}")
    x += 1

# Declare a dictionary with string keys and mixed value types
students: dict[str, any] = {
    "first number": 20,
    "second number": 40,
    "number": "test"
}

# Declare a list of dictionaries
all_students: list[dict] = [{
    "name": "test",
    "james": "two"
}, {
    "lastname": "james"
}]

# Check if "number" exists in the dictionary and print its value
if students.get("number", None) is not None:
    print(f"Number is not null it value is: {students['number']}")

# Access and print elements of the list of dictionaries
print(all_students[0]["name"])
print(all_students[0].get("james"))

def add_numbers(a: int = 0, b: int = 0) -> int:
    """Add two numbers and return the result."""
    return a + b

# Basic operations and type annotations
new_number: int = add_numbers(4, 6)

def greet(name: str) -> str:
    return f"Hello, {name}!"

# List comprehension
numbers: List[int] = [1, 2, 3, 4, 5]
squares: List[int] = [n ** 2 for n in numbers]
print(f"Squares: {squares}")

# Dictionary comprehension
square_dict: Dict[int, int] = {n: n ** 2 for n in numbers}
print(f"Square dictionary: {square_dict}")

# Lambda functions
multiply: Callable[[int, int], int] = lambda x, y: x * y
print(f"4 * 5 = {multiply(4, 5)}")

# Map function
doubled: List[int] = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled}")

# Filter function
evens: List[int] = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Decorator usage
print(greet("Alice"))

from typing import Dict, List, Any, Set, Tuple
from collections import namedtuple, defaultdict, Counter

# Integer
my_int: int = 42
print(f"My integer: {my_int}")

# Float
my_float: float = 3.14
print(f"My float: {my_float}")

# String
my_str: str = "Hello, Python!"
print(f"My string: {my_str}")

# List
my_list: list[int] = [1, 2, 3, 4, 5]
print(f"My list: {my_list}")

# Dictionary
my_dict: dict[str, str] = {"key1": "value1", "key2": "value2"}
print(f"My dictionary: {my_dict}")

# Tuple
my_tuple: tuple[int, str, float] = (1, "a", 3.14)
print(f"My tuple: {my_tuple}")

# Set
my_set: set[int] = {1, 2, 3, 4, 5}
print(f"My set: {my_set}")

# None
none_value : None = None
if none_value is None:
    print("none_value is None")

# Object model
class MyClass:
    def __init__(self, value: str):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


my_object = MyClass("Hello")
my_object.display()

# Tuples
point: Tuple[int, int] = (3, 4)
x, y = point
print(f"Point: {point}, x: {x}, y: {y}")

# Sets
unique_numbers: Set[int] = {1, 2, 3, 4, 4, 5, 5}
print(f"Unique numbers: {unique_numbers}")

# Named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])
alice: Person = Person('Alice', 30, 'New York')
print(f"Person: {alice}")
print(f"Name: {alice.name}")

# Default dict
word_count: defaultdict[str, int] = defaultdict(int)
words: List[str] = ["apple", "banana", "apple", "cherry", "banana", "date"]
for word in words:
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")

# Counter
fruit_counter: Counter = Counter(words)
print(f"Fruit counter: {fruit_counter}")
print(f"Most common fruit: {fruit_counter.most_common(1)}")

# List operations
numbers: List[int] = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.extend([7, 8])
print(f"Numbers: {numbers}")
print(f"Sliced numbers: {numbers[2:5]}")

# Dictionary operations
person: Dict[str, Any] = {
    "name": "Bob",
    "age": 25,
    "city": "London"
}
person.update({"job": "Developer", "age": 26})
print(f"Person: {person}")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")

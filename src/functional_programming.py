from typing import List, Callable, Any
from functools import reduce

def apply_operation(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def compose(*funcs: Callable) -> Callable:
    def compose_two(f: Callable, g: Callable) -> Callable:
        return lambda x: f(g(x))

    return reduce(compose_two, funcs, lambda x: x)

# Map
numbers: List[int] = [1, 2, 3, 4, 5]
squared: List[int] = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Filter
even_numbers: List[int] = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Reduce
sum_of_numbers: int = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers: {sum_of_numbers}")

# Higher-order functions
add: Callable[[int, int], int] = lambda x, y: x + y
multiply: Callable[[int, int], int] = lambda x, y: x * y

print(f"10 + 5 = {apply_operation(add, 10, 5)}")
print(f"10 * 5 = {apply_operation(multiply, 10, 5)}")

# Function composition
def double(x: int) -> int:
    return x * 2

def increment(x: int) -> int:
    return x + 1

double_then_increment: Callable[[int], int] = compose(increment, double)
increment_then_double: Callable[[int], int] = compose(double, increment)

print(f"Double then increment 5: {double_then_increment(5)}")
print(f"Increment then double 5: {increment_then_double(5)}")

# Partial application
from functools import partial

def power(base: int, exponent: int) -> int:
    return base ** exponent

square: Callable[[int], int] = partial(power, exponent=2)
cube: Callable[[int], int] = partial(power, exponent=3)

print(f"Square of 5: {square(5)}")
print(f"Cube of 5: {cube(5)}")

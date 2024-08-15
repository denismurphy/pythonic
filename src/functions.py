# Initialize an empty list to store student names
students: list[str] = []

# Prompt the user to enter a student name and store it in _student_name
student_name = input("Enter student name:")
print(student_name)


# Function to return a random number (for demonstration purposes)
def get_random_number() -> int:
    return 42


# Function to add a student name to the _students list
def add_student(student: str) -> None:
    students.append(student)


# Function with default arguments for first and last name
def default_args(first_name: str = "Denis", last_name: str = "Murphy") -> None:
    print(f"My name is {first_name} {last_name}")


# Function accepting variable-length argument list (varargs)
def var_args_list(*args: any) -> None:
    for arg in args:
        print(arg)


# Function accepting variable-length keyword arguments (kwargs)
def var_args_dict(**kwargs: any) -> None:
    print(f"height: {kwargs['height']}")
    print(f"description: {kwargs['description']}")
    print("Now Print all")
    for arg in kwargs:
        print(f"arg:{arg}, value:{kwargs[arg]},")

# Call the function with default arguments
default_args()
# Call the function with a custom first name
default_args(first_name="Caroline")
# Call the function with a custom last name
default_args(last_name="Crazy")
# Call the function with a list of variable arguments
var_args_list(None, "Hello", 1.2)
# Call the function with a dictionary of keyword arguments
var_args_dict(height="10.1", description="Hello", test="Extra")


# Outer function demonstrating nested function and nonlocal keyword
def outer_function() -> None:
    name: str = "Denis"
    print(f"name is {name}")

    # Inner function to modify the outer function's variable
    def inner_function() -> None:
        nonlocal name
        name = f"{name} Murphy"

    # Call the inner function to modify the 'name' variable
    inner_function()  # appends "Murphy" to end of name variable
    print(f"name is {name}")


# Call the outer function
outer_function()

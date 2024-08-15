import builtins
from builtin_types import MyClass

def print_type_match(value: any):
    type_of_value = type(value)
    match type_of_value:
        case builtins.str:
            print(f"{value} is a String")
        case builtins.int:
            print(f"{value} is an Int")
        case builtins.float:
            print(f"{value} is an Float")
        case _: # Default case
            print("\nNever Gonna Give You Up!!!")

# Generate a dictionary for type to message mapping
type_messages: dict[type:str] = {
    type_: f"is a {name.capitalize()}"
    for name, type_ in vars(builtins).items()
    if isinstance(type_, type)
}

def print_type_dict(value: any):
    # Get the type of the value
    type_of_value = type(value)
    # Lookup the message in the dictionary, default to a custom message
    message = type_messages.get(type_of_value, "\nNever Gonna Give You Up!!!")
    print(f"{value} {message}")

# hello is a Str
print_type_dict(value="hello")

# 200 is a Int
print_type_dict(value=200)

# 20.5 is a Float
print_type_dict(value=20.5)

# True is a Bool
print_type_dict(value=True)

# [1, 2, 3] is a List
print_type_dict(value=[1, 2, 3])

# {0: 'Home'} is a Dict
print_type_dict(value={ 0 : "Home" })

# Never Gonna Give You Up!!!
print_type_dict(value=MyClass("Hello"))

# Declare a list of integers
bytes1: list[int] = [1, 2, 3]

# Create a bytearray from the list of integers
bytearray1: bytearray = bytearray(bytes1)

# Declare another list of integers
bytes2: list[int] = [1, 2, 3]

# Create a bytearray from the second list of integers
bytearray2: bytearray = bytearray(bytes2)

# Compare the two bytearrays for equality
are_they_the_same: bool = bytearray1 == bytearray2

# Print the result of the comparison
print(f"are they the same? {are_they_the_same}")

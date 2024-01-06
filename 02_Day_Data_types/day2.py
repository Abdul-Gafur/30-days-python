# Day 2 - Python data types


# Text type - str
# Numeric types - int, float, complex
# Sequence types - list, tuple, range
# Mapping Type
# Set type
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Types: NoneType

# Lets start by defining some data types

name = "Ali" # String datatype
x = 20       # Int datatype
x = 20.5     # Float datatype
x = 20j      # Complex datatype
fruits = ["apple", "bannana", "cherry"]  # List datatype
fruits = ("apple", "bannana", "cherry")  # Tuples datatype
x = range(6) # Range datatype
x = {"name": "John", "age": 30} # Dictionary datatype
x = True # Boolean datatype

# print(type(x))

### Numeric datatype
# int, float, complex

### Type conversions
x = 1 # int
y = 2.8 # float
z = 1j  # complex

convertx = float(x)
print(type(convertx))

### Random Number
import random
print(random.randrange(1, 10))
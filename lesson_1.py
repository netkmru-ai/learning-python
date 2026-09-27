"""
Lesson 1: Python Basics
=======================

Welcome to your first Python lesson! Run this file with:

    python3 lesson_1.py

Read through the comments, look at the output, then try the exercises
at the bottom. Lines starting with `#` are comments -- Python ignores them.
"""


# ---------------------------------------------------------------------------
# 1. Printing output
# ---------------------------------------------------------------------------
# print() shows text on the screen. Text goes inside quotes ("..." or '...').
print("Hello, world!")
print('Single quotes work too.')
print("You can print several things at once:", 1, 2, 3)


# ---------------------------------------------------------------------------
# 2. Variables
# ---------------------------------------------------------------------------
# A variable is a name that stores a value. Use `=` to assign.
name = "Ada"
age = 36
print("Name:", name)
print("Age:", age)

# Variables can be changed later.
age = age + 1
print("Next year,", name, "will be", age)


# ---------------------------------------------------------------------------
# 3. Basic data types
# ---------------------------------------------------------------------------
whole_number = 42          # int   -> whole numbers
decimal_number = 3.14      # float -> numbers with a decimal point
greeting = "Hi there"      # str   -> text (a "string")
is_learning = True         # bool  -> True or False

# type() tells you what kind of value something is.
print(type(whole_number))
print(type(decimal_number))
print(type(greeting))
print(type(is_learning))


# ---------------------------------------------------------------------------
# 4. Arithmetic
# ---------------------------------------------------------------------------
a = 17
b = 5
print("a + b  =", a + b)    # addition        -> 22
print("a - b  =", a - b)    # subtraction     -> 12
print("a * b  =", a * b)    # multiplication  -> 85
print("a / b  =", a / b)    # division        -> 3.4 (always a float)
print("a // b =", a // b)   # floor division  -> 3   (drops the remainder)
print("a % b  =", a % b)    # remainder       -> 2
print("a ** 2 =", a ** 2)   # power           -> 289


# ---------------------------------------------------------------------------
# 5. Working with strings
# ---------------------------------------------------------------------------
first = "Grace"
last = "Hopper"

# Join strings with +
full_name = first + " " + last
print(full_name)

# f-strings: put an `f` before the quotes and variables inside { }
print(f"{first} has {len(first)} letters in her first name.")

# Handy string methods
print(full_name.upper())    # GRACE HOPPER
print(full_name.lower())    # grace hopper
print("  padded  ".strip()) # removes spaces at the ends -> "padded"


# ---------------------------------------------------------------------------
# 6. Converting between types
# ---------------------------------------------------------------------------
number_text = "10"
number = int(number_text)       # "10" (text) -> 10 (int)
print(number + 5)               # 15

price = 9.99
print("Price: " + str(price))   # convert a number to text before joining


# ---------------------------------------------------------------------------
# 7. Making decisions with if / elif / else
# ---------------------------------------------------------------------------
temperature = 22

if temperature > 30:
    print("It's hot!")
elif temperature > 15:
    print("It's pleasant.")
else:
    print("It's cold.")

# Note: the indented lines (4 spaces) belong to the `if` block above them.
# Comparison operators: ==  !=  <  >  <=  >=


# ---------------------------------------------------------------------------
# 8. Getting input from the user (optional)
# ---------------------------------------------------------------------------
# input() pauses and waits for the user to type something.
# It always returns a string. Uncomment the lines below to try it:
#
# your_name = input("What is your name? ")
# print(f"Nice to meet you, {your_name}!")


# ---------------------------------------------------------------------------
# Exercises -- try these yourself!
# ---------------------------------------------------------------------------
# 1. Create a variable `city` with the name of your city and print
#    "I live in <city>" using an f-string.
#
# 2. Store the length and width of a rectangle in two variables and
#    print its area and perimeter.
#
# 3. Write an if/else that prints "even" if a number is even and "odd"
#    otherwise. Hint: use the % operator.
#
# 4. Ask the user for their birth year with input(), convert it to an int,
#    and print how old they will be in 2030.

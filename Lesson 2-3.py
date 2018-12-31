# Define and call Functions

# Basic Function Syntax:
# def function_name(args):
#     statements
# Remember:
# Don't forget def or the colon.
# Indentation is important (discussed next).
# args is zero or more arguments.

# Function Example:
def pr_values(a, b, c):
    print('a is', a)
    print('b is', b)
    print('c is', c)
    return a + b + c
# Calling pr_values(1, 2, 3) returns the value 6, after printing 1, 2, 3.

# Indentation Matters:
# The basic rule in Python is that all code at the same level of the
#     program (such as the top level of a function) must have matching indentation.
# Beware of tabs! Tabs do not equal spaces!
# Python uses indentation to determine what statements are in the same
#     block rather than "begin" and "end" syntax.

# Pythagoras (Demo):
def pythag(a,b):
    sq_a = a * a
    sq_b = b * b
    return (sq_a + sq_b) ** 0.5
# Note that variables can be created through assignemnt.
# these will be local unless you use "global" keyword to prevent that.

# Global vs. Local Variables:
# By using the "global" keyword, you preven an assignment inside a 
#     function from making it local.
amount = 1000
def set_amount:
    global amount
    amount = 2000
set_amount()
print(amount)

# Returning Multiple Values:
# In Python, there are no true "pass-by-value" or "pass-by-reference"
#     arguments, so passing back values would seem to be impossible.
#     But you can return multiple values.
# Example:
def make_data():
    return 1, 2, 3
a, b, c = make_data()

# Default Arguments:
# Default arguments specify a default value, so the argument need not be specified.
# All default arguments must follow all others.
# Example:
def make_value(a, b = 0):
    return a + b
# make_value(3) returns 3

# The Forward Reference Problem:
# When a funciton is EXECUTED, all referneces must be resolved.
#     This means taht any function called by THIS function must be defined somewhere.
# But what if A calls B and B calls A?
# Solution: Just define all your functions first, becuase you execute any of them.
#     That way, you cannot go wrong.

# Doc Strings for Functions:
# To create a document string, place a literal string right after the heading and indent.
# For example:
def foo(a, b, c):
    '''This is a foo function.'''
    return a + b + c

# Doc String Example (Demo):
def Pythag(a, b):
    '''Pythagorean Formula:
    Returns lenth of hypotenuse.'''
    return (a * a + b * b) ** 0.5
help(Pythag)    # Prints the literal string

# Saving a Program (Demo):
# Copy a function or other code.
# From IDLE menu, choose File -> New.
# Paste the code and edit.
# From IDLE menu, choose File -> Save.
# Choose a name with a .py extension.
# In the future, this program can be run by first choosing File -> Recent Files.

# Summary (Functions):
# When you enter a function, remember the def keyword, name, arg, list, and colon (:).
# IDLE will automatically indent. In any case, keeping consistent indenting is critical.
# Pass-by-value and pass-by-refernce are not support for arguments.
#     However, you can return multiple argument values, if you want.
# Default arguments, if included, come last.
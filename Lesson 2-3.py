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
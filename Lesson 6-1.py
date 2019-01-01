# Understand errors and the runtime environment

# Category #1: Syntax Errors:
# A synteax error is just a case of applying the grammar incorrectly.
# It is frequently caused by typos or omitted punctuation. For example:
a, b, c = 1, 2, 3
print(a b c)        # Missing commas!

# Category #2: Runtime Errors (Exceptions):
# A runtime error is detected only when executed.
# Python is asked to do something impossible or unreasonable, such as divide
#     by zero or open a non-existent file.
# An exception (for example ZeroDivisionError) is raised and must be handled,
#     or the program quits.
# Documentation on Build-in Exceptions: 
#     docs.python.org/3/library/exceptions.html

# Category #3: Program Logic Errors:
# With a program logic error (or just logic error), the program seems to run
#     correctly but it doesn't do what you want, or it gives incorrect results.
# Only way to detect these errors is to relentlessly test the program.
# These errors are the most challenging of all, because the fault could lie anywhere.

# Let's Debug a Program (demo):
# Let's debug by figuring out why 1, 1, is not printed first, and how do we fix this?
def Fibo(n):
    a = b = 1
    while a < n:
        a, b = a + b, a
        print(a, end = ' ')
# set a = 1, b = 0 and print statment needs to come first in the while loop

# Debugging Tools:
# Debugging Tools are not a "magic bullet."
# All that debugging commands do is:
#     Allow you to step through the program more slowly.
#     Give you access to all variables without having to print them.
# But while this is a convenience, it doesn't really save you from the hard
#     work of trying to analyze what went wrong and why.

# Running from the Command Line (Demo):
# Enter a program:
def Pythag(a, b):
    '''Pythagorean Theorem.'''
    return (a * a + b * b) ** 0.5
Pythag(3,4)
# Copy and save as pythag.py.
# Start Terminal application.
# Change directory, if needed, to Documents folder.
# Enter python pythag.py

# Accessing Command-Line Args:
# Import the sys package:
import sys 
# Command-line args are available as the list
sys.argv 
# The first element, sys.argv[0], is the name of the program file. The other
#     elements of the list, if any, will be arguments.

# Command-Line Args (Demo):
import sys
if len(sys.argv) >= 3:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
else:
    a = b = 1
print(Pythag(a, b))

# Using pydoc:
# pydoc is a utility downloaded with Python.
# pydoc is the command-line equivalent to help from within the interactive environment.
# For example, from the command line: pydoc pythag
# Press "Q" to exit the help that is displayed.

# Summary (Errors):
# We get three kinds of errors in Python. 
# Syntax errors: The prgogramming code makes no sense, as it isn't even grammatical.
# Runtime errors (exceptions): You're asking the computer to do something it
#     isn't willing or can't do.
# Program logic errors: Program runs, but it produces all the wrong results.
#     These are the hardest of all to catch and resolve.
# Handle exceptions

# Exceptions and Examples:
# Remember, exceptions generally represent runtime errors: Python is asked
#     to so something unreasonable or impossible when a statement is executed.
# Examples:
# ZeroDivisionError
# FileNotFoundError
# IndexError

# Syntax for try/except:
# A try block is executed unconditionally; but if specified exception is raised,
#     control passes to the corresponding except block. 
#     (Note: You may have multiple except clauses.)
try:
    statements
except exception_name:
    statements

# Extensions: else and finally:
# The else clause is executed if the try block finishes execution without
#     any exception being raised.
# The finally clause is executed afterward.
else:
    statements
finally:
    statements

# Exception Handling Files (Demo):
try:
    f = open('stuff.txt', 'r')
    print(f.read())
except:
    print('File I/O error.')
else:
    print('Operation success!')
finally:
    f.close()

# File-Read with Input Loop:
while True:
    try:
        fname = input('Enter file: ')
        if not fname:
            break
        f = open(s)
        print(f.read())
        f.close()
        break
    except FileNotFoundError:
        print('File not found. Re-enter.')

# Summary (Handling Exceptions):
# Use of try and except are the main tools. Any exception raised during the 
#     try statements can be handled by an except block.
# The else clause is executed on success.
# The finally clause is executed after the other blocks are - usually closes all resources.


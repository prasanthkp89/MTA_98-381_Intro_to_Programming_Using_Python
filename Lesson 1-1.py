# Perform Python assignments

# Simple Python Program Demo:
a = 1
b = 2
print(a + b)

# Basic rules of Assignment:
# var_name = expression
# Rules: 
# 1) The expression is entirely evaluated first.
# 2) Any var. in expression must be defined.
# 3) var_name becomes a name for the expression; 
#    var_name is created if it doesn't already exist. 
#    If it does exist, it is reassigned.

# Assignment Fail Demo:
a = 1
b = 2
c = a + b   # This is okay
d = c + x   # Fail! What is x? NameError: name 'x' is not defined
# Fixing the assignment
x = 100
d = c + x   # Now this works

# What is a Variable?:
# In most languages, we'd say that a variable is a 
#     "named storage location."
# But that is NOT TRUE for Python!
# In Python, a variable is just a name. That means 
#     it has no attributes, and no memory location,
#     until it is assigned as a name for a piece of data
#     - that data supplies the attributes.
# Remember, a variable is just a name!

# Assignment Ops (Part 1):
# The following is legal, as long as the first statement is present...
n = 5
n = n + 1   # n gets the value 6
n = n + 1   # n gets the value 7

# Assignment Ops (Part 2):
# Combined add/asign is so common, Python has shortcuts...
n += expr   # n = n + expr (add)
n *= expr   # n = n * expr (mult)
n -= expr   # n = n - expr (sub)
n /= expr   # n = n / expr (div)

# Assignment Ops (Part 3):
# So, for example, the earlier example can be replaced by:
n = 5
n += 1      # n gets the value 6
n += 1      # n gets the value 7

# Rules for Variable Names:
# First character must be an underscore (_) or letter.
# Subsequent characters must be an underscore (_), letter, or digit.
# No embedded spaces. No keywords, such as "if", "while", "def", "for",
#     "and", "or", "else".
# All names in programs are case sensitive:
#      "dog" should not be confused with "DoG". 

# Adding Comments:
# A comment consists of everything from the hash tag (#) - outside
#     a quoted string - to the end of a line.
# A comment is simply ignored by Python itself.
a = b       # a assigned val. of b

# Summary (Python Assignments):
# In Python, assignments are the primary way to create a variable
#     (which is just a name for a piece of data).
# The attribute of a variable is the attribute of the data that it names.
# Comments may be used to help a programmer read the program,
#     but they are only as good as the text you write!
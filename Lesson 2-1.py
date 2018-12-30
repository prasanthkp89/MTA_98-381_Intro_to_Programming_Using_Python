# Construct Python strings

# Four Ways to Write Strings:
# Single quote marks: 'I am a string.'
# Double quote marks: "I am a string."
# Triple (literal) quote marks (these are used in doc strings,
#     as we'll see, and can be multiline): '''I am a string.'''
# Raw string, which preserves all characters as they are: 
#     r'This is a backslash: \'

# Quotes and Embedded quotes:
# Single quoted strings can embed double quotes:
#     'I am the "Walrus," said Paul.'
# Double quoted strings can embed single:
#     "I'm the Walrus, said Paul."
# Literal can embed both, plus multiline:
#     '''I'm telling you, the "Walrus" was Paul.'''

# Backslash (\) Creates Escape Sequences:
# Using escape sequences is another way to embed quotation marks.
s = 'I\'m the Walrus!'
# Also, some values (such as newlines) are embedded with escape sequences.
s = 'Line One\nLine Two\nLine Three'

# Quote Marks Not Part of String:
# Whichever may be the choice of quotation marks used, they are not a 
#     part of the string itself, but only a part of how the string is
#     represented in code. This is why printing a string omits the quote marks.
print('Hello')      # Returns Hello

# General Properties of Strings:
# Strings automatically have as much space as needed.
# Strings can be concatenated:
s = 'banana' + 'fish'       # Will not put a space in unless specified
# The str class supports many methods, including s.upper(), s.lower(), s.strip().
# Strings are immutable, which means you can't change part of a string; 
#     you must create an entirely new string and reassign it. 

# Example of String Reassignment:
s = 'Big '
s = s + 'Ugly '
s = s + 'Fish'
print(s)        # Prints 'Big Ugly Fish'
# This works because "s" is assigned an entirely new string each time.
# You cannot modify or change part of an existing string. We are simply
#     reassigning the variable name, "s"!

# Formatting Techniques:
# The string format method enables you to create individual print fields,
#     which are then filled in by arguments to format. Example:
s = '{} + {} = {}.'
print(s.format(1, 2, 3))
# This prints: 
#     1 + 2 = 3.

# String Comparisons (is vs. ==):
# The is keyword tests to see if two variables refer to the same actual
#     object in memory. For example:
s1 = s2 = 'dog'
s1 is s2    # usually returns True
# This is unreliable. Usually much better to use "==", which tests contents
#     regardless of where they are stored:
'dog' == "dog"      # returns True

# Greater & Less Than Comparisons:
# Strings can be the subject of greater than and less than comparisons.
# Words are evaluated to CODE PAGE order, but this is usually consistent
#     with alphabetical ordering.
'Abe' < 'Brian'     # Returns True

# Summary (Strings):
# There are at least three ways of writing a string in Python.
# Which technique you use (single quotes, double quotes, literal)
#     determine how easy it is to embed quote marks.
# However, you can also use backslash (\).
# Strings are immutable, but assignment of an entire string gets around the problem.

# Build and manage lists

# List Examples:
# Let's say you wanted to list all the scores in an Olympic competition.
[8.9, 8.8, 9.5, 7.2, 9.0, 8.0]
# Members of a rock band:
['John', 'Paul', 'George', 'Ringo']

# Lists Can Mix Data:
# For example, you can freely mix strings and numbers:
[1, 2, 3, 'John', 'Paul', 3.14]
# Such lists cannot be sorted in Pyton 3.0
# Lists can contain other lists, creating 2-D lists.
[[1,2], [2,4], [3, 6, 9]]

# Creating a List with Append:
# You can start out with an empty list.
my_list = []
# Add members by calling append.
my_list.append('Moe')
my_list.append('Larry')
my_list.append('Curly')
# List is now: ['Moe', 'Larry', 'Curly']

# Indexing Lists:
# Lists can be positively indexed (0 to N-1).
# As with strings, they can also use negative indexes (-1 to -N).
# 'John'    'Paul'    'George'    'Ringo'
#    0         1          2          3
#   -4        -3         -2         -1

# Slicing Lists:
# Rules for slicing lists are similar to those for slicing strings.
#     Result is a new list.
my_list[a:b]    # From position "a" up to but not including position "b"
my_list[a:]     # First "a" elements
my_list[:b]     # From beginning up to but not including position "b"
my_list[a:b:c]
my_list[:]      # Member-by-member copy

# List Slicing Examples (Demo):
a_lst = ['John', 'Paul', 'George', 'Ringo']
a_lst[1:3]      # From second element up to, not including last.
                # Returns ['Paul', 'George']
a_lst[:2]       # First two elements.
                # Returns ['John', 'Paul']
a_lst[-2:]      # Last two elements.
                # Returns ['George', 'Ringo']

# Sorting Lists:
a_lst = ['John', 'Paul', 'George', 'Brian']
a_lst.sort()    # Produces a new list ['Brian', 'George', 'John', 'Paul']

# Using the "in" Keyword:
beat_lst = ['John', 'Paul', 'George', 'Ringo']
'John' in beat_lst      # Returns True
'Pete Best' in beat_lst # Returns False
# Case sensitive

# The min and max Functions:
# These functions work only on sortable lists, so the elements must
#     have compatible types.
# The min function returns the lowest element.
min(list)
# The max function returns the highest element.
max(list)

# The len and sum Functions:
# The len function always works, and returns the number of top-level elements.
len(list)
# The sum function only works on numeric types. For example, the following
#     produces 6:
sum( [1, 2, 3] )

# The remove Method:
# Remember, all methods use the obj.method() syntax.
# The remove method removes the first element equal to the value.
beatles_lst.remove('Pete')
# Python raises exception if you try to remove an element that is not
#     currently a member of list.

# Lists vs. Tuples:
# Tuples can do most things lists can do, but they have a different syntax:
[1, 2, 3]       # This is a list
(1, 2, 3)       # This is a tuple
1, 2, 3         # Also a tuple (often)
# However, tuples are immutable and do not support any of the methods or 
#     functions that modify contents.

# Olympic Score Function (Demo):
def final_score(a_lst):
    ilow = min(a_lst)
    a_lst.remove(ilow)
    ihigh = max(a_lst)
    a_lst.remove(ihigh)
    return sum(a_lst)/len(a_lst)        # Note: original list altered!
my_lst = [8.2, 8.3, 2.3, 9.9, 7.0]
print(final_score(my_lst))          # Prints 7.83333333333333
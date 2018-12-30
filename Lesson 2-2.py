# Perform indexing and slicing string operations

# Non-negative Indexes:
# Indexes are a way of referring to individual characters by number.
# In Python, indexes usually run from 0 to N-1 where N is the number
#     of characters. (Nonnegative indexes are zero-based.)
s1 = 'TheBeatles'
# T h e B e a t l e s
# 0 1 2 3 4 5 6 7 8 9

# Negative Indexes:
# In Python, you can ALSO refer to individual characters by using
#     negative indexes. These run from -1 to -N.
# They can be interchanged with pos. indexes.
#   T   h   e   B   e   a   t   l   e   s
# -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

# Simple Indexing Examples:
# The first character can always be indexed as string[0]. Therefore:
s = 'Hello'
print(s[0])     # Print H
print(s[1])     # Print e

# Indexes Cannot Be Used to Modify:
# Remember that strings are immutable.
# Therefore, the following is not valid:
s = 'hello'
s[0] = 'H'      # Error! String is immutable!!
# However, the following is valid.
s = 'Hello'     # Assigning an entirely new value to the variable 

# Slicing Syntax:
# Slicing a string does not throw out-of-bounds exceptions.
#     It supports following varieties:
string[a:b]     # Position a UP TO but no including b.
string[a:]      # Position a up to end.
string[:b]      # Beginning up to but not including b.
string[:]       # Copy whole string.  

# Examples of Slicing (Demo):
my_str = 'DragonFly'
my_str[0:6]     # 'Dragon'
my_str[:6]      # 'Dragon'
my_str[-3:]     # 'Fly'
#   D   r   a   g   o   n   F   l   y
#   0   1   2   3   4   5   6   7   8
#  -9  -8  -7  -6  -5  -4  -3  -2  -1

# Third Slicing Argument:
# In the expression string[a:b:c], "c" tells how many characters to 
#     advance each time. It may even be negative.
# If "c" is negative, the direction changes. Therefore, the following 
#     gets the reverse of a string:
rev_str = my_str[::-1] 

# Palindrome Example (Demo):
# Because string[::-1] reverses a string, we can use this to test for palindromes.
a_str = 'racecar'
a_str == a_str[::-1]     # True

# Uppercase Vs. Lowercase:
# The upper() method produces a new string all uppercase (except non-letter characters).
# The lower() method produces a string all lowercase (except non-letter characters).
s = 'racecar'
print(s.upper())        # RACECAR

# Stripping a String:
# By default, the strip method strips all leading and trailing spaces,
#     but not characters "within."
# For example:
s = '       Henry VIII      '
# s.strip() prints 'Henry VIII'

# Summary (Indexing & Slicing Strings):
# Indexing a string gets a single element.
# Indexes must be in a range.
# Non-negative indexes run from 0 to N-1.
# Negative indexes run from -N to -1 (reverse direction).
# Slicing is a way of getting a part of a string. Note that indexes in 
#     a slice can be out of range.
# s[a:b] contains chars starting with a, up to but not including position b.

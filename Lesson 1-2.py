# Understand numeric and Boolean data types

# Integers vs Floating Point:
# Integers have no fractional portion, but they are always 
#     absolutely precise. Examples: 2, -10, 3000, 1.
# Floating point numbers have a fractional portion but potentially 
#     have rounding errors. Examples of floating-point: 2.5, -100.7,
#     2.35e27, 1.0

# "Infinite Integers" in Python:
# Integers in Python have no limit other than that imposed by the 
#     limitations of the system.
# So integers can store astronomical values, far beyond the limits of
#     32 or 64 bit integers. And you need to do nothing special to 
#     get these.
# For example, a "google" (googol) is 10 to the 100th, far bigger
#     than the number of particles in the universe.

# Google vs. Google + 1 (Demo):
g = 10 ** 100   # 10 to the 100th
print('{:,}'.format(g))     # Prints g with comma separators
g == g + 1      # True or False? (This if false)
# Note there's a big difference between = (assign) vs. == (test for equality)!!

# Integers, Objects, and Methods:
# What's an object? Simply put, an object is a data type through which
#     you can call special functions, called "methods."
# Methods, as opposed to functions, are called this way, using "dot notation."
#     object_name.method_name(arguments)
# In Python, the golden rule is that every piece of data is an object.

# Objects and Methods (Part 2):
# what does it mean to say that every piece of data is an object?
# It means that every object supports "methods" supplied by Python.
# You can see a list of methods supported for integers by typing:
#     help(int)

# Integer Methods (Demo):
(5).bit_lenth()     # Returns 3
(8).bit_length()    # Returns 4
'{:b}'.format(8)    # Returns '1000' (prints 8 in binary)
# Why doesn't 5.bit_length() work?
#     5 followed by a dot assumes it is a floating point number

# Pros and Cons of Floating Point:
# Floating point numbers contain a fractional portion.
# (However, 1.0 and 2.0 are floating point format even though having no fraction.)
# The drawback is that floating pointing numbers have limited precision,
#     leading to rounding errors in the case of very large or tiny numbers.

# Division in Python 2.0 vs. 3.0:
# In Python 2.0, at least one operand must be floating-pt to get
#     a floating-pt result: for example, 2/3.0
# In Python 3.0, "/" produces regular divsion and "//" produces "floor division."
3 / 5       # Returns 0.6
3//5        # Returns 0
3 % 5       # Returns 3
            # modulus division
            # => remainder after div.

# Operator Precendence:
# 1) "Dot" operator, parentheses
# 2) (highest) Exponentiation Operator: "**"
# 3) Multiplication, Division, Mod Operators:
#       "*" "/" "//" "%"
# 4) Addition and Subtraction: "+" "-"
# 5) Comparison, Boolean operators (explained later)
# 6) Assignment and Combined Assignment Ops

# Operator Precedence (Examples):
2 ** 3 * 10 + 5 * 2     # Equivalent to ((2 **3) * 10) + (5 * 2)
x *= 2 + 3      # Not equivalent to  x = x * 2 + 3, but x = x * (2 + 3)

# Boolean Data
# Boolean data is either True or False. It's important in if, while, and 
#     for as we'll see.
# We saw this with the comparison, g == g + 1
# But other types of data automatically convert to bool type as needed
bool(n)     # Returns true if n is any nonzero number
bool(0)     # Returns false
bool()      # Returns false. Same as bool(None)

# Boolean Operators:
# Operator          Description
#   ==              Test for equality
#   !=              Not equal test
#   >               Greater than
#   <               Less than
#   >=              Greater than or equal
#   <=              Less than or equal
#   and             Logical AND (short circuit)
#   or              Logical OR
#   xor             Logical Exclusive OR
#   not             Logical negation

# Remember, Variables are Just Names:
# The same name (x in this case) can be a name for any kind of data at any time!
# However, this would be terrible programming practice!
x = 1
x = 'I am a string'
x = [10, 22, 44.5]

# Naming Conventions:
# Therefore, adopting a strong set of conventsions is strongly recommended.
# Many names are given to integers, but especially n, m, i, j, k.
# Names for floating point values may begin with "x" or "y".
# Strings are s, s1, s2, s3, etc. or xxx_str.
# Lists are xxx_lst.

# Summary (Numeric Types)
# The most common numeric types in Python are integer and floating-point.
# Integers in Python are "infinite".
# Floating point's main advantage is that it can hold fractions; integers cannot.
# But integers are absolutely precise, floating point numbers are not.
# Boolean (True/False) is also important.
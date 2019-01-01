# Manage flow with loops

# For Loops Used with Lists:
for loop_var in collection:
    statements
# Action is to repeat statements once for each item in collection.
#     For example, to print each element:
for n in [1, 1, 3, 5, 8, 13, 21]:
    print(n)

# The range Function:
# range(n) produces a list [0, 1, 2, ... n-1]
# range(n, m) produces [n, n+1, ... m-1]
# You can therefore use range(n) to index all the elements in a list, "C style."
#     For example:
b_list = ['John', 'Paul', 'George']
for i in range(len(b_list)):
    print(b_list[i])

# Another Look at Ranges:
# These are equivalent:
for i in range(len(b_list)):
    print(b_list[i])
for i in [0, 1, 2]:
    print(b_list[i])
# However, do NOT use this approach when you can just loop through a list directly!

# Appropriate Use for Ranges:
# The following for statement prints all the numbers from 0 to 8:
for i in range(9):
    print(i)
# Factorial function:
prod = 1
for i in range(1, n+1):
    prod *= i

# The "while" Loop:
# While loops are even simpler than for loops.
# Executes as long as the condition holds true.
#           Is condition true?
#         no                yes
#        done           execute statements
#                       Is condition true?
#                        no          yes
#                             ...

# Review: What is "True"?
# For integers and floating point, 0 values convert to False and non-zero
#     convert to Boolean True.
# For lists, empty lists convert to False and all other lists all convert
#     to Boolean True.
# For strings, empty strings convert to False and all other strings convert to True.
# So the following means execute if "s" is empty:
if not s:
    do_something()

# While Loops and "break":
# The "break" keyword causes Python to break out of the nearest enclosing for 
#     or while loop.
# This enables "infinite loops" to exit. For example:
while True:
    # Do some stuff.
    if not s:
        break

# Adding Machine (Demo):
sum = 0
while True:
    s = input('Enter number: ')
    if not s:
        break
    sum += float(s)
print('The sum is', sum)

# Fibonacci Numbers (Demo):
def Fibo(n):
    a = b = 1
    while a < n:
        a, b = a + b, a
        print(a, end = ' ')
Fibo(100)       # Returns Fibonacci numbers until they exceed 100

# Summary (Loops):
# The for keyword enables you to step through a list; for each element, the 
#     statement block is executed once, each time setting the loop variable 
#     to a different element.
# The while keyword is simpler. It is like if except that the block is executed 
#     until the condition is not true.
# Use the break keyword to exit early.
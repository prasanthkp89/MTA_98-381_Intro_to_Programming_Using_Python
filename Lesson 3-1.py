# Perform conversion, input, and output

# Getting Input:
# Syntax of an input statement:
# input_str = input(prompt_str)
# Example:
name_str = input('Enter your name:')

# Type Conversion is Necessary:
# Any two numbers can be added together: 
25 + 0.19
# Strings can be concatenated together: 
'banana' + 'fish'
# However, adding a number to a string causes an exception: 
'5' + 5.0       # Error!

# Converting String to int:
# Get a number from the console:
s = input('Enter number: ')
# Convert to int format:
n = int(s)
# Now we can do math on the number:
print('n squared is', n * n)

# Convert to float:
s = '3.141592'
pi = float(s)       # Pi is a number.
print('Sq. root of pi is', pi ** 0.5)

# Temp. Conversion (Demo):
def conv_temp():
    s = input('Enter Cent.: ')
    cent = float(s)
    fahr = cent * 1.8 + 32.0
    print('Fahr equiv. is', fahr)
conv_temp()         # Execute function.

# The print Function:
# The print function takes any number of arguments.
print(args)
# The sep argument changes the default for placing spaces between arguments.
# The end argument indicates what is printed after the last argument.

# Example Print (Demo):
a, b, c, = 'Big', 'Ugly', 'Fish'
print(a, b, c, sep='', end='!!')
# THis prints BigUglyFish!!

# Summary (Conversion and I/O):
# You can use the input statement to both prompt for input and retrieve 
#     it from end-user.
# The output that comes back is a string.
# However, this string must be converted to int or float if it is to be 
#     used for arithmetic, as opposed to string, operations.
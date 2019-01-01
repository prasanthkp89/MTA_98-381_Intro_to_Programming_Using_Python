# Read a file

# Reading from a Text File:
# You can read an entire file by calling the file_obj.read() method.
# You can also read in a list of lines by calling the file_obj.readlines() method.
# If you read in individual lines, they include the trailing newline (\n).
#     This can be stripped.

# Reading a File (Demo):
f = open('stuff.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()

# Reading a File #2 (Demo):
f = open('stuff.txt', 'r')
str_list = f.readlines()
for s in str_list:
    s = s.strip('\n')
    print(s)
f.close()

# The "with" Keyword:
# Using the "with" keyword guarantees taht a file objects is closed 
#     successfully at the end of a block, even if an exception is raised. 
# Example:
with open('stuff.txt', 'r') as f:
    file_contents = f.read()
    print(file_contents)

# Files Sources of Errors:
# When you open a file for reading, the files must exist. 
#     (Note: these are all runtime errors).
# When you open a file for writing, Python will erase its contents and 
#     create a new one. But the file specification must be vaild.
# When you open a file, it must be available for I/O operations. 
#     Files that are already open may not necessarily be successfully 
#     opened agian.

# Summary (File I/O):
# As with other languages, you can use the following 3-step procedure:
#     open a file, read or write, close.
# Or you can use the with keyword to reduce some of this verbosity.
# It helps to learn the modes as well as you can... "t" and "b" for text and 
#     binary (text is the default); then "r", "w", and "a".
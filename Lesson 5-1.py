# Open and write to a text file

# Opening a File:
# You must open a file to get the file object.
# You can then use this object to read or write a file.
file_obj = open(file_name, mode)
# Perform read and write ops.
file_obj.close()

# File modes (Add "b" for binary):
# 'w'   Text file write
# 'r'   Text file read
# r+    Open file for reading and writing; start at beginning of file.
# w+    Open for reading and writing; Create file if it doesn't exist; otherwise truncate.
# a     Open for appending: write at tend of file. Create file if it doesn't exist.
# a+    Similar to "a", but file position is at the beginning.

# Text Vs. Binary Mode:
# Text mode is easiest in most respects. A text file is, conceptually,
#     just a series of characters.
# The only organization in a text file is lines, differentiate by newlines ('\n').
# Binary mode contains raw data and may have any organization.
#     The easiest way to do binary I/O is to use the pickle package.

# Writing to a Text File:
# Call the file_obj.write() method.
# Argument is a text string.
# If you want to write the string as an entire "line", you'll need
#     to append a newline.
# To append a newline, concatenate '\n'

# Text File Write (Demo):
f = open('stuff.txt', 'w')
while True:
    s = input('Enter>>')
    if not s:
        break
    f.write(s + '\n')
f.close()


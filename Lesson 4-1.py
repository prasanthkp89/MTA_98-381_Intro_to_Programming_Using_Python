# Manage flow with decisions

# Simple "if" Statement in Python:
# if condition:
#    statements
# Notes:
# Indentation still matters.
# Condition can be any object, but Booleans (with True/False value) preferred.
# All of statements are executed or none are.

# Example "and" Operator:
# Same example:
if age > 40:
    print('Getting up there.')
    is_old_timer = True
# Example with "and":
if age > 12 and age < 20:
    print('You are a teenager.')
    is_teenager = True

# Example "else":
if age > 12 and age < 20:
    print('You are a teenager.')
    print('Have fun!')
else:
    print('You are not a teenager.')

# Using "elif":
s = input('Ender a cmd. number: ')
cmd = int(s)
if cmd == 1:
    do_cmd_1()
elif cmd == 2:
    do_cmd_2()
elif cmd == 3:
    do_cmd_3()
else:
    do_cmd_4()

# Important Points to Review:
# The "if" portion is mandatory
# You may have any number of "elif" clauses: either zero, one, or many.
# You may have AT MOST one "else" clause.
# The "else" clause is the "default" action.
# Each statement block can have one or more statements. Use pass as a 
#     no-op if you need to.

# Nested "if" Statements:
# Because the statements inside an if-block are statements like any other,
#     they can also be if statements.
# The result is a "nested" if statement.
# Python lets you nest control structures (if, while, and for) to any level.
#     You'd run out of screen space long before you exhausted the system's limit.

# Are You a Cool Teenager? (Demo):
# Assume age, fave assigned vals.
if age > 12 and age < 20:
    if fave == 'Beatles':
        print("You're a cool teen!")
    else:
        print("Uncool teen!")
else:
    print("You are not a teenager.")
    print("You are young or old.")

# Summary (Decisions):
# The if, elif, and else keywords support decision making.
# Such a structure must have one if clause.
# It may have zero or more elif clauses.
# It may have zero or one else clauses.
# Don't foreget the colon.
# Again, indentation matters!
# Nesting supported to any level.
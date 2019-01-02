# Use Python packages

# Using the math Package (Demo):
import math
help(math)
math.sqrt(2.0)
# This is approx 1.41421....
math.atan(1) * 4
# This should produce pi
math.pi

# Using time & datetime (Demo):
import time
import datetime 
help(time)
time.time()
time.time()
datetime.datetime.now()

# Using the sys Package (Demo):
import sys
help(sys)
sys.stdout.write('Hello!')
s = sys.stdin.readline()
Hamlet
s
'Hamlet\n'
# sys also used for cmd-line args

# The os and os.path Packages (demo):
import os
import os.path
os.path.isfile('stuff.txt')
os.path.getsize('stuff.txt')
os.remove('stuff.txt')

# Using the random Package (demo):
import random
help(random)
random.random()
# A real number between 0 and 1.0
random.randint(1, 100)
# An integer from 1 to 100, inclusive

# Number Guessing Game (Demo):
import random
n = random.randint(1, 100)
while True:
    guess = int(input('Enter a guess: '))
    if guess > n:
        print('Too high! Guess again!')
    elif guess < n:
        print('Too low! Guess again!')
    else:
        print('Success!')
        break

# Summary, Packages:
# You can import packages in a couple of different ways:
import package_name
from package_name import *
from package_name import item
# The first technique is definitely preferred.
# Learn what random, os, os.path, math and sys are all good for. 
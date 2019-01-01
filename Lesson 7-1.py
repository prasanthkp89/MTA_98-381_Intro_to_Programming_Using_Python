# Import Python packages

# How to Import Packages:
# Import module the simple way:
import package_name
# Now, all functions and objects from the package must be qualified to be used:
package_name.func_name()

# Importing Individual Functions:
# To importat one function at a time:
from package import func_name
# To import all functions and objects:
from package import *
# The problem with these approaches is that they make "name conflicts" likely.
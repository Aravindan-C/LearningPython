__author__ = 'aravindan'

"""As your programs grow in size,you will want to break them into multiple files for easier maintainance To create a module,put the relevant statements and definitions into a file that has the same name as the
module/file must have a .py suffix"""

# file : div.py
def divide(a,b):
    q=a/b  # if a and b are integers,q is an integer
    r=a-q*b
    return (q,r)
# To use your module in other programs,you can use the import Statement

import div
a,b =div.divide(2305,29)

from div import divide
a,b = divide (2305,29)
print a,b

# To load all of a module's contents into the current namespace,you  can also use the following
from div import *
import string
print dir(string)
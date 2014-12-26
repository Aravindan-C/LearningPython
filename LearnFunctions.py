__author__ = 'aravindan'
"""Use def statement to create a function"""
def remainder(a,b):
    q=a//b          # // is truncating division.
    r=a-q*b
    return r
print remainder(20,15)


"""To invoke a function,simply use the name of the function followed by its arguments enclosed in parentheses"""

def divide(a,b) :
    q=a//b
    r=a-q*b
    return (q,r)
quotient,remainder = divide(1456,33)
print quotient,remainder

"""default values are given in a function definition,they can be ommitted from subsequent function callls"""
def coonect (hostname,port,timeout=300)
    #function body
connect('www.python.org',80)

connect(port=80,hostname="www.python.org")   #To invoke functions using keyword arguments
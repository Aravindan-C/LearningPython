__author__ = 'aravindan'
# file : div.py
def divide(a,b):
    q=a/b  # if a and b are integers,q is an integer
    r=a-q*b
    return (q,r)
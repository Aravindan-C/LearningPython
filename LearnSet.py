__author__ = 'aravindan'
"""A set is used to contain an unordered collection of objects,To create a set use the set() function and supply a sequence of items such as follows"""

s= set([3,5,9,10,10,11])      # create a set of unique  numbers
t=set("Hello")       # create a set of unique characters
u=set("abcde")
"""sets are unordered and cannot be indexed by numbers"""
print t ^ u
print s & u
t.add('x')  # To add an item to a set
s.update([9,10,11],[9,14,16]) # To add a multiple item to set
print s
t.remove('H','l')
t.remove('e')
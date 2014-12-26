__author__ = 'aravindan'
"""Instead of returning a single value, a function can generate an entire sequence of results if it uses yield statement"""

def countdown(n):
    print "counting down!"
    while n>0:
        yield n  # Generate a value (n)
        n -=1
"""Any function that uses yield known as a generator"""
for i in  countdown(10):
    print i,


"""Generators are an extremely powerful way of writing programs based on processing pipelines streams or data floe."""
__author__ = 'aravindan'
"""You Can pack a collection of object together into a single object using a tuple)"""
stock = ('GOOG',100,490.10)
address = ('www.python.org',80)
first_name="ABCD"
last_name="HFJK"
person = first_name,last_name,9500397672
"""Unpack tuples -Extacted by numerical index just like a list"""
name,shares,price = stock
host,port = address
first_name,last_name,phone = person
print name,host,phone

"""Supports-indexing,slicing and concatenation Unsupports-replace,delete,append new elements)"""
"""Tuples are immutable , They use a more compact representation where there is no extra space"""
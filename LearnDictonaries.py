__author__ = 'aravindan'


"""Dictonary is an associative array or hash table that contains objects indexed by keys"""
stock ={"name" : "GOOG", "shares" : 100, "price" : 490.10}

"""To access members of a dictonary,use the key-indexing operator as follows"""

name=stock["name"]
value=stock["shares"]* stock["price"]
print value

"""Inserting or modifying objects works like this"""
stock["shares"] =75
stock["date"] ="June 7,2007"
print stock
prices = {"GOOG" : 490.10,"AAPL" :123.50,"IBM" :91.50,"MSFT" :52.13}
if "GOOG" in prices :
    p= prices ["GOOG"]
else:
    p=0.0
print p
"""To obtain a list of dictionary keys,convert a dictionary to list"""
syms=list(prices)
print syms
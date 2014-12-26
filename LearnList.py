__author__ = 'aravindan'

names = ["Dave" ,"Mark","Ann","Phil"]
print names
a=names[2]
print a
names[0]="jeff"
print names
names.append("Paula") # To append new items to end of a list
print names
names.insert(2,"Thomas") # To insert an item into middle of a list
print names

"""An Empty list created in two ways"""

CreateList1=[]
CreateList2=list()

"""List Can contain any kind of python object including other lists"""
b=[1,"Dave",3.14,["Mark",7,9,[100,101]],10]
print b[1]
print b[2]
print b[3]
print b[0]
print b[3][3]
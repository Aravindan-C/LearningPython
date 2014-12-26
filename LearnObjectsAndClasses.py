__author__ = 'aravindan'
"""All values used in a program are objects,An object consist of internal data and metods that perform various kinds of operations involving that data"""
items=[37,42]
print items


"""dir() function list the metods available on an object and is a useful tool for interactive experimentation"""
items1=items.__add__([73,101])
print items1


"""The Class statement is used to define new types of objects and for object-oriented programming"""

#class defines a simple stack with push(),pop(),length()

class Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)
s=Stack()
s.push("Dave")
print s.pop()
s.push(42)
s.push ([3,4,5])
print s.pop()
print s.pop()
__author__ = 'aravindan'
# compare two objects

a=5
b=2
def compare(a,b):
    if a is b:
        print "a and b are the same objects"
    if a==b:
        print "a and b have the same value"
    if type(a) is type(b):
        print ("a and b have the same types %s" )%( type(a))
    if  isinstance(a,int):
        print a

compare(a,b)

"""isinstance() function is aware of inheritance,it is the preferred way to check the type of any python object"""
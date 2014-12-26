__author__ = 'aravindan'
try:
    f=open("file.txt","r")
except IOError as e:
    print e
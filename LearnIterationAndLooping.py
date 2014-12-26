__author__ = 'aravindan'
for n in [1,2,3,4,5,6,7,8,9,0]:
    print "2 to the %d power is %d" % (n,2**n)
for n in range(1,10) :
    print "2 to the %d power is %d" % (n,2**n)

a= range(5)
b=range(1,8)
c=range(0,14,3)
d=range(8,1,-1)
print a,b,c,d

a= "Hello World"
# print out the individual characters in a
for c in a :
    print c

b=["Dave","Mark","Ann","Phill"]
#Print out the members of a list
for name in b:
    print name

c={'GOOG' :490.10,'IBM' :91.50,'AAPL' :123.15}
#Print out all of the members of a dictionary
for key in c:
    print key,c[key]

#Print all  of the lines in a file
f=open("foo.txt")
for line in f:
    print line
principal = 10000    # Initial amount
rate = 0.05         # Interest rate
numyears = 5        # Number of years
year = 1
f = open("out.txt","w")
while year <= numyears:
    principal = principal * (1+rate)
    print >>f,"%3d %0.2f" % (year,principal)
    f.write("%3d %0.2f\n" %(year,principal))
    """print format(year,"3d"),format(principal,"0.2f")"""
    year +=1
f.close
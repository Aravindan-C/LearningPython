__author__ = 'aravindan'
filename = "portfolio.csv"
portfolio=[]
for line in open(filename):
    fields = line.split(",")   #split each line into a list
    name = fields[0]    #Extract and Convert individual fields
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name,shares,price)  # create a tuple (name ,shares , price)
    portfolio.append(stock)      #Apeend to list of records
    print portfolio
    print portfolio[0][1]
total=0.0
for name,shares,price in portfolio:
    total +=shares*price
print total
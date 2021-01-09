# The city's system carries 1,200,000 people each day.How many people does the bus system carry each year?(1 Year=365 days)
# solve without using *,/ operator,bitwise operator or loop
def multiply(x,y):
    if(y==0):
        return 0
    if(y>0):
        return (x+multiply(x,y-1))
    if (y<0):
        
        return -multiply(x,y)

peopleTravelDaily=1200000;
dayOfYear=365;
peopleTravelYearly=multiply(peopleTravelDaily,dayOfYear);
print(peopleTravelYearly)
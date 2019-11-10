from  datetime import datetime
from random import randrange


now = datetime.now()
print now
#num=input('Enter the no of random numbers to print')
i=0
num=10000
while i<num:
    r = randrange(10000)
    print r
    i +=1
nw= datetime.now()
print nw
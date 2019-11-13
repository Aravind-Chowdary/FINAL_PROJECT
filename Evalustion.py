from  datetime import datetime
from random import randrange
import random
import string

stringLength=10
letters = string.ascii_lowercase
str_1= ''.join(random.choice(letters) for i in range(stringLength))
print(str_1)
now = datetime.now()
print(now)
#num=input('Enter the no of random numbers to print')
i=0
num=10000
while i<num:
    r = randrange(10000)
    print (r)
    i +=1
nw= datetime.now()
print (nw)
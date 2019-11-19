from  datetime import datetime
from random import randrange
import random
import string

def key_gen(l):

    k=randrange(2**l,2**(l+1))
    return k


print("Encryption started")
now = datetime.now()
print(now)
num = 10000001
i = 0
while i<num:
        k=key_gen(48)
        p=round(k**0.75)
        r=randrange(p,k-p)
        m =randrange(10000)
        k=64
        c=m*k+r
        i += 1
print ("Encryption ended")
nw=datetime.now()
print nw
diff=nw-now
print (diff)
def dec(k, c):
    return c/k



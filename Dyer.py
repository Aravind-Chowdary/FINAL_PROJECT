from  datetime import datetime
from random import randrange
import random
import string

def key_gen(l):

    k=randrange(2**l,2**(l+1))
    return k


def enc(k):
    print("Encryption started")
    now = datetime.now()
    print(now)
    #stringLength = 16
    num = 100000
    i = 0
    while i<num:
        p=round(k**0.75)
        r=randrange(p,k-p)
        #letters = string.ascii_lowercase
        #m = ''.join(random.choice(letters) for i in range(stringLength))
        m =randrange(10000)
        c=m*k+r
        return c
    print ("Encryption ended")
    nw=datetime.now()
    print (nw)
def dec(k, c):
    return c/k



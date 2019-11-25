
from Dyer import *
import time


def key_gen(l):

    k=randrange(2**l,2**(l+1))
    return k

def eval():
    i=0
    k=key_gen(48)
    total=0
    num=100000
    while i<num:
        m=randrange(10000)
        start=time.time()
        enc(k,m)
        end=time.time()
        total +=end-start
    print ("Time taken for the encryption:", total)



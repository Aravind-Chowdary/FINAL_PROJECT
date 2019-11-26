from Popa_cli import *
import random
import time

key=key_gen()

iv=init_vect()

i=0
total=0
num=10000
while i<num:
    data=random.getrandbits(16)
    start=time.time()
    enc(key, iv, data)
    end=time.time()
    total +=end-start
print("TIme for Encryption", total)

j=0
taken=0
eum=10000
while i<eum:
    data=random.getrandbits(16)
    begin=time.time()
    encd=enc(key, iv, data)
    dec(key, encd, iv)
    close=time.time()
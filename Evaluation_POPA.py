from Popa_cli import *
import random
import time

key=key_gen()

iv=init_vect()

i=0
taken_enc=0
num=10000
while i<num:
    data=random.getrandbits(16)
    start=time.time()
    enc(key, iv, data)
    end=time.time()
    taken_enc +=end-start
    i +=1
print("TIme for Encryption", taken_enc)

j=0
taken=0
eum=10000
while i<eum:
    data=random.getrandbits(16)
    begin=time.time()
    encd=enc(key, iv, data)
    dec(key, encd, iv)
    close=time.time()

from Dyer import *

import time


i=0
k=key_gen(48)
total=0
num=100000
while i<num:
    f=open('rands.txt')
    m=f.readline()
    start=time.time()
    enc(k,m)
    end=time.time()
    total +=end-start

print ("Time taken for the encryption:", float(total)/float(num))

j=0
taken=0
eum=10000
while i<eum:
    m=randrange(10000)
    begin=time.time()
    c=enc(k,m)
    dec(k, c)
    close=time.time()
    taken += close-begin
    print ("Time taken for both encryption:", taken)




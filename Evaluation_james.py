
from Dyer import *

import time

i = 0
k = key_gen(48)
total = 0
num = 10000
f = open('rands.txt', 'r')
while i < num:
    w = f.readline()
    m=int(w)
    start = time.time()
    d=enc(k, m)

    end = time.time()
    total += end-start
    i += 1
print ("Time taken for the encryption:", float(total)/float(num))
f.close()


from Boldyreva import *

import time

key = OPE.generate_key(32)
OPE = OPE(key, in_range=ValueRange(1, 2 ** 16 - 1), out_range=ValueRange(1, 2 ** 31 - 1))

i = 0

total = 0
num = 10000
f = open('rands.txt', 'r')
while i < num:
    w = f.readline()
    m=int(w)
    start = time.time()
    d=OPE.encrypt(m)
    end = time.time()
    total += end-start
    i += 1
print ("Time taken for the encryption:", float(total)/float(num))
f.close()

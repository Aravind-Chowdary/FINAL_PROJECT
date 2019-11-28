
from Dyer import *

import time


i = 0
k = key_gen(48)
total = 0
num = 1
f = open('rands.txt', 'r')

while i < num:
    m = f.readlines()
    int (m)
    start = time.time()
    enc(k, m)
    end = time.time()
    total += end-start
    i +=1
print ("Time taken for the encryption:", float(total)/float(num))


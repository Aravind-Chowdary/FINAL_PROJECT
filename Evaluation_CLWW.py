from My_CLWW import *
from random import randrange
import time
chen=chen.NEW()

i=0
k=chen.key_gen()
total=0
num=100000
while i<num:
    m=randrange(10000)
    h=chen.pre(k, m)
    begin=time.time()
    chen.ore_enc(k,m)
    end=time.time()
    total +=end-begin
print ("Time taken for the encryption:", float(total)/float(num))
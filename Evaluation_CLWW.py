from CLWW import *


import time

cnt = 0
num = 10000
i=0
total=0
passwd = rnd_word(10)
while i < num:
    num1 = random.randrange(2**63, 2**64)
    num2 = random.randrange(2**63, 2**64)
    start = time.time()
    a = ore_enc(bin(num1)[2:], passwd)
    b = ore_enc(bin(num2)[2:], passwd)
    end = time.time()
    total += end-start
    i += 1
print ("Time taken for the encryption:", float(total) / float(num))

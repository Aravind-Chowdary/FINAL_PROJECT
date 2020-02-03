
from Kerschbaum import *

import time


class evalution():

    Ker = Kersch(2, 16)

    def eval(self):

        i = 0
        total = 0
        num = 10000
        f = open('rands.txt', 'r')
        while i < num:
            w = f.readline()
            m=int(w)
            start = time.time()
            d=self.Ker.enc(m)
            end = time.time()
            total += end-start
            i += 1

        print ("Time taken for the encryption:", float(total)/float(num))

        f.close()
        return
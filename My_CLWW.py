from Crypto import Random
from Crypto.Hash import HMAC,SHA256


class chen:
    h = None
    k = None

    def __init__(self):
        self.k=self.key_gen()
        self.h=HMAC.new(self.k, digestmod=SHA256)

    def key_gen(self):
        k=Random.get_random_bytes(64)
        return k

    def prf(self, m):
        if m is "":
            return m
        self.h.update(m)
        td=self.h.digest()
        return td

    def ore_enc(self,  m):
        b = bin(m)
        b= b[2:]
        ab = ""
        ct1 = ()
        for i in b:
            ab += i
            x = self.prf(ab[:-1])
            y = ab[-1]
            ct1 += str((str(x) + str(int(y) % 3))),
        return ct1

    def ore_compare(self, ct1, ct2):
        if ct1 == ct2:
            return 0
        L = len(ct1)
        cnt = 0
        while ct1[cnt] == ct2[cnt]:
            cnt += 1
        g= ct1[cnt]
        print g
        q = (int(g) + 1) %3
        w = int(ct2[cnt])
        if q == w:
            return -1
        else:
            return 1
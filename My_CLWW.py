from Crypto.Random import random
from Crypto.Hash import HMAC,SHA256

class chen:
    def __init__(self):
        h=None
        k=None

    def key_gen(self):
        k=random.get_random_bytes(64)
        return k

    def pre(self, k, m):
        h=HMAC.new(k,m,digestmod=SHA256)
        return h.digest()

    def ore_enc(self, k, m):
        ab = ""
        ct1 =()
        for i in m:
            ab += i
            ct1 += str((self.pre(ab[:-1], k) + int(ab[-1])) % 3)
        return ct1

    def ore_compare(self, ct1, ct2):
        if ct1 == ct2:
            return 0
        L = len(ct1)
        cnt = 0
        while ct1[cnt] == ct2[cnt]:
            cnt += 1
        if (int(ct1[cnt]) + 1) % 3 == int(ct2[cnt]):
            return -1
        else:
            return 1
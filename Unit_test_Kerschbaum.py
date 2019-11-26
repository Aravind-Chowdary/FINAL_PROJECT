import unittest

from Kerschbaum import  n, T, encrypt, decrypt


class SimpleTestCase(unittest.TestCase):
    n==16
    T=={}
    from Kerschbaum import calc_max
    max=calc_max(10)

    def testConsistency(self):
        x=85785
        c = encrypt(x,T,-1,max)
        d = decrypt(c,T)
        assert d ==x




if __name__ == "__main__":
    unittest.main()

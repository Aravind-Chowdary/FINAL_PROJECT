import unittest

from Kerschbaum import *
Kersch=Kersch()


class SimpleTestCase(unittest.TestCase):
    Kersch.n==16
    Kersch.T=={}

    max=Kersch.calc_max(10)

    def testConsistency(self):
        x=85785
        c = Kersch.encrypt(x,Kersch.T,-1,max)
        d = Kersch.decrypt(c,Kersch.T)
        assert d ==x




if __name__ == "__main__":
    unittest.main()

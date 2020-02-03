import unittest

from Kerschbaum import *


class SimpleTestCase(unittest.TestCase):
    Kersch = Kersch(2, 16)

    def testConsistency(self):
        x=85785
        c = self.Kersch.enc(x)
        d = self.Kersch.dec(c)
        assert d ==x




if __name__ == "__main__":
    unittest.main()

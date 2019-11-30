import unittest

from Boldyreva import *


class SimpleTestCase(unittest.TestCase):

    key = OPE.generate_key(32)
    OPE=OPE(key, in_range=ValueRange(1,2**16-1) , out_range=ValueRange(1,2**31-1))

    def testConsistency(self):
        plt=49166
        plaintext=int(plt)
        c = self.OPE.encrypt(plaintext)
        d = self.OPE.decrypt(c)
        assert d == plaintext



if __name__ == "__main__":
    unittest.main()

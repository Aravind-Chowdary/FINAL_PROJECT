import unittest

from Boldyreva import *


class SimpleTestCase(unittest.TestCase):
    key = OPE.generate_key(32)
    OPE=OPE(key, in_range=ValueRange(1,2**16-1) , out_range=ValueRange(1,2**31-1))


    def testConsistency(self,):
        plaintext=4916684
        c =OPE.encrypt(plaintext)
        d = OPE.decrypt(c)
        assert d == plaintext



if __name__ == "__main__":
    unittest.main()

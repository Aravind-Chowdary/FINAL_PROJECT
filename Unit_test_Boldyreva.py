import unittest



from Boldyreva import *


class SimpleTestCase(unittest.TestCase):
    OPE=OPE.NEW()

    OPE.generate_key(32)

    def testConsistency(self,):
        plaintext=4916684
        c =OPE.encrypt(plaintext)
        d = OPE.decrypt(c)
        assert d == plaintext



if __name__ == "__main__":
    unittest.main()

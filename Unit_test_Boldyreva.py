import unittest



from Boldyreva import *


class SimpleTestCase(unittest.TestCase):
    OCC=OPE.__new__(object)

    #OPE.generate_key(32)

    def testConsistency(self,):
        plaintext=4916684
        c =OCC.encrypt(plaintext)
        d = object.decrypt(c)
        assert d == plaintext



if __name__ == "__main__":
    unittest.main()

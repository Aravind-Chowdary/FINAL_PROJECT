import unittest



from Kerschbaum import calc_max,  n, T, encrypt, decrypt


class SimpleTestCase(unittest.TestCase):
    n==13
    T=={}
    max=calc_max(10)

    def testConsistency(self):
        x=85785
        c = encrypt(x,'gary',6,max)
        d = decrypt(c,T.t)
        assert d ==x




if __name__ == "__main__":
    unittest.main()

import unittest
import random

from My_CLWW import *


class SimpleTestCase(unittest.TestCase):

    chen = chen()

    def testOrderPreserving(self):
        k = self.chen.key_gen()
        m1 = random.randint(1, 65535)
        m2 = random.randint(1, 65535)
        c1 = self.chen.ore_enc(m1)
        c2 = self.chen.ore_enc(m2)
        if m1 < m2:
            assert self.chen.ore_compare(c1, c2) == -1
        if m1 > m2:
            assert self.chen.ore_compare(c1, c2) == 1
        if m1==m2:
            assert self.chen.ore_compare(c1, c2) == 0


if __name__ == "__main__":
    unittest.main()

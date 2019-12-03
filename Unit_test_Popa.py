import unittest
import random
import string
from Popa_cli import *


class SimpleTestCase(unittest.TestCase):
    pop_cli=pop_cli()
    key = pop_cli.key_gen()
    iv= pop_cli.init_vect()
    OPETree=OPETree.new()
    letters = string.ascii_lowercase
    m = ''.join(random.choice(letters) for i in range(10))

    def testConsistency(self):
        letters = string.ascii_lowercase
        m = ''.join(random.choice(letters) for i in range(10))
        c = self.pop_cli.enc(self.k,self.iv, m)
        d = self.pop_cli.dec(self.k,self.iv, c)
        assert d == m


if __name__ == "__main__":
    unittest.main()

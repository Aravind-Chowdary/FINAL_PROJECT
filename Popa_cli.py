from Crypto.Random import random
from Crypto.Cipher import AES
from Popa_ser import *


class pop_cli:

    OPEobj = OPETree()

    def key_gen(self):
        key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        return key

    def init_vect(self):
        iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])  # This needs to be involved in enc function(doubt)
        return iv

    def enc(self,  iv, data):
        global OPEobj
        aes = AES.new(self.key_gen(), AES.MODE_CBC, self.init_vect())
        # data = 'hello world 1234'   <- 16 bytes
        encd = aes.encrypt(data)
        self.OPEobj.insert_in_tree(encd)
        return encd

    def dec(self, key,encd, iv):
        aes = AES.new(key, AES.MODE_CBC, iv)
        decd = aes.decrypt(encd)
        return decd
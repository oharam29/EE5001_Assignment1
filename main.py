#!/usr/bin/python
import binascii
import unittest

import PRESENT_Test
from AES import *
from AES_Test import *
from PRESENT import *
from PRESENT_Test import *

class Test_AES(unittest.TestCase):
    def test(self):
        print("AES - Test 1")
        master_key = 0x2b7e151628aed2a6abf597aed9cf4f3c
        self.AES = AES(master_key)
        plaintext = 0x3243f6a8885a308d313198a2e0370734
        encrypted = self.AES.encrypt(plaintext)
        print(encrypted)
        if encrypted == 265986203824032857909769280400137674588:
            print("Encrypted")
        print("AES - Test 1 Finished")


    def test2(self):
        print("AES - Test 2")
        master_key = 0x3243f6a8885a308d313198a2e0370734
        self.AES = AES(master_key)
        plaintext = 0x2b7e151628aed2a6abf7158809cf4f3c

        encrypted = self.AES.encrypt(plaintext)
        print(encrypted)
        if encrypted == 137980941141787771488758467738391517272:
            print("Encrypted")
        print("AES - Test 2 Finished")

class Test_PRESENT(unittest.TestCase):
    def test(self):
        print("PRESENT - Test 1")
        master_key = b"0000000000"
        self.Present = Present(master_key, 32)
        plaintext = b'hello'
        encrypted = self.Present.encrypt(plaintext)
        print(encrypted)
        print("PRESENT - Test 1 Finished")




if __name__ == '__main__':
    unittest.main()
    #AES_Test.Test_All()
    #PRESENT_Test.Test_AddRoundKey()
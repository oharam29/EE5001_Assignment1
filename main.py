#!/usr/bin/python
import binascii
from AES import *
from PRESENT import *

master = 0000000000000
if __name__ == '__main__':
    GenerateRoundKey((master))
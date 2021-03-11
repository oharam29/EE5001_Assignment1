import binascii


Sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

PBox = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
        4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
        8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
        12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

def GenerateRoundKey(key):
    roundKeys = []
    for i in range(1, 32):
        roundKeys.append(key >> 16)
        key = ((key * (2 ** 19 - 1)) << 61) + (key >> 19)
        key = ((Sbox[key >> 0x4c] << 0x4c) + (key & (2 ** 0x4c - 1)))
        key ^= i << 15
    #print(roundKeys)
    return roundKeys


def addRoundKey(state, round_key):
    return state ^ round_key


def sBoxLayer(state):
    result = 0
    for i in range(16):
        result += Sbox[( state >> (i*4)) & 0xF] << (i*4)

    return result

def pLayer(state):
    result = 0
    for i in range(64):
        result = result + ((state >> i ) & 0x01) << PBox[i]
    return result


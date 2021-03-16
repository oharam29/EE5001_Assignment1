import binascii
# tables needed for the trasnformation
Sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

PBox = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
        4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
        8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
        12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

# round key generator
def GenerateRoundKey(key):
    roundKeys = []
    for i in range(1, 32):
        roundKeys.append(key >> 16)
        key = ((key * (2 ** 19 - 1)) << 61) + (key >> 19)
        #key = (Sbox[key >> 76] << 76) + (key & (2 ** 76 - 1))
        key ^= i << 15
    return roundKeys


# 3 transformation funcitons:
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
        result = result + ((state >> i) & 0x01) << PBox[i]
    return result

#funnctions to convert form string to int and vice versa, created using old undergrad python notes
def number2string(i):
    string = '%0*x' % (8*2, i)
    return binascii.unhexlify(str(string))

def string2number(i):
    val = int.from_bytes(i, byteorder='big')
    return val

class Present:

    def __init__(self, key, rounds):
        self.rounds = rounds

        if len(key) * 8 == 80:
            self.round_keys = GenerateRoundKey(string2number(key))
        else:
            raise ValueError("Key incorrect length")

    def encrypt(self, text):
        state = string2number(text)
        for i in range(self.rounds-1):
            state = addRoundKey(state, self.round_keys[i])
            state = sBoxLayer(state)
            state = pLayer(state)
        encrpyted = addRoundKey(state,self.round_keys[-1])
        return number2string(encrpyted)
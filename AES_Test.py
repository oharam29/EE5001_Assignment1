from AES import *

def Test_SubBytes():
    init_state = [[25, 61, 227, 190], [160, 244, 226, 43], [154, 198, 141, 42], [233, 248, 72, 8]]

    subbed_state = [[212, 39, 17, 174], [224, 191, 152, 241], [184, 180, 93, 229], [30, 65, 82, 48]]

    subBytes(init_state)
    assert (init_state == subbed_state)
    print("SubBytes - Test passed")

def Test_ShiftRows():
    init_state = [[212, 39, 17, 174], [224, 191, 152, 241], [184, 180, 93, 229], [30, 65, 82, 48]]

    shifted_state = [[212, 191, 93, 48], [224, 180, 82, 174], [184, 65, 17, 241], [30, 39, 152, 229]]

    shiftRow(init_state)
    assert (init_state == shifted_state)
    print("Test Passed")

def Test_AddRoundKey():
    init_state = [[50, 67, 246, 168], [136, 90, 48, 141], [49, 49, 152, 162], [224, 55, 7, 52]]
    key=[[43, 126, 21, 22], [40, 174, 210, 166], [171, 247, 21, 136], [9, 207, 79, 60]]

    roundkey_added = [[25, 61, 227, 190], [160, 244, 226, 43], [154, 198, 141, 42], [233, 248, 72, 8]]
    addRoundKey(init_state, key)
    assert(init_state == roundkey_added)
    print("Test Passed")


def TEST_Mix():
    init_state = [[46, 7, 125, 3]]

    mixed= [191, 180, 65, 39]

    mix_all(init_state)
    assert(init_state == mixed)
    print("MixAll - Test Passed")

def Test_All():
    Test_SubBytes()
    Test_AddRoundKey()
    TEST_Mix()
    Test_ShiftRows()
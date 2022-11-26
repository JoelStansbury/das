# Table of Position of 64 bits at initial level: Initial Permutation Table
initial_perm = [
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    60,
    52,
    44,
    36,
    28,
    20,
    12,
    4,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    64,
    56,
    48,
    40,
    32,
    24,
    16,
    8,
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
]

# Expansion D-box Table
exp_d = [
    32,
    1,
    2,
    3,
    4,
    5,
    4,
    5,
    6,
    7,
    8,
    9,
    8,
    9,
    10,
    11,
    12,
    13,
    12,
    13,
    14,
    15,
    16,
    17,
    16,
    17,
    18,
    19,
    20,
    21,
    20,
    21,
    22,
    23,
    24,
    25,
    24,
    25,
    26,
    27,
    28,
    29,
    28,
    29,
    30,
    31,
    32,
    1,
]

# Straight Permutation Table
per = [
    16,
    7,
    20,
    21,
    29,
    12,
    28,
    17,
    1,
    15,
    23,
    26,
    5,
    18,
    31,
    10,
    2,
    8,
    24,
    14,
    32,
    27,
    3,
    9,
    19,
    13,
    30,
    6,
    22,
    11,
    4,
    25,
]

# S-boxes table
sbox = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

# Final Permutation Table
final_perm = [
    40,
    8,
    48,
    16,
    56,
    24,
    64,
    32,
    39,
    7,
    47,
    15,
    55,
    23,
    63,
    31,
    38,
    6,
    46,
    14,
    54,
    22,
    62,
    30,
    37,
    5,
    45,
    13,
    53,
    21,
    61,
    29,
    36,
    4,
    44,
    12,
    52,
    20,
    60,
    28,
    35,
    3,
    43,
    11,
    51,
    19,
    59,
    27,
    34,
    2,
    42,
    10,
    50,
    18,
    58,
    26,
    33,
    1,
    41,
    9,
    49,
    17,
    57,
    25,
]

# --parity bit drop table
keyp = [
    57,
    49,
    41,
    33,
    25,
    17,
    9,
    1,
    58,
    50,
    42,
    34,
    26,
    18,
    10,
    2,
    59,
    51,
    43,
    35,
    27,
    19,
    11,
    3,
    60,
    52,
    44,
    36,
    63,
    55,
    47,
    39,
    31,
    23,
    15,
    7,
    62,
    54,
    46,
    38,
    30,
    22,
    14,
    6,
    61,
    53,
    45,
    37,
    29,
    21,
    13,
    5,
    28,
    20,
    12,
    4,
]

# Number of bit shifts
shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Key- Compression Table : Compression of key from 56 bits to 48 bits
key_comp = [
    14,
    17,
    11,
    24,
    1,
    5,
    3,
    28,
    15,
    6,
    21,
    10,
    23,
    19,
    12,
    4,
    26,
    8,
    16,
    7,
    27,
    20,
    13,
    2,
    41,
    52,
    31,
    37,
    47,
    55,
    30,
    40,
    51,
    45,
    33,
    48,
    44,
    49,
    39,
    56,
    34,
    53,
    46,
    42,
    50,
    36,
    29,
    32,
]


def dec2bin(num):

    res = bin(num).replace("0b", "")

    if len(res) % 4 != 0:
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = "0" + res
    return res


def bin2dec(binary):
    return int(binary, 2)


def hex2bin(s):
    map_of_h2b = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    res = ""
    for i in range(len(s)):
        res = res + map_of_h2b[s[i]]

    return res


def bin2hex(s):
    h = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }

    res = "".join(h[s[i : i + 4]] for i in range(0, len(s), 4))
    return res


def LS(bit_string, num_of_shifts):
    s = ""
    for i in range(num_of_shifts):
        for j in range(1, len(bit_string)):
            s = s + bit_string[j]
        s = s + bit_string[0]
        bit_string = s
        s = ""
    return bit_string


def RS(bit_string, num_of_shifts):
    for i in range(num_of_shifts):
        bit_string = bit_string[-1] + bit_string[:-1]

    return bit_string


def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result = result + "0"
        else:
            result = result + "1"
    return result


def get_round_key_encrypt(key):
    round_keys = []

    # PC-1
    key = "".join(key[i - 1] for i in keyp)

    # C0
    left_key = key[:28]
    # D0
    right_key = key[28:]
    for round_count in range(16):
        left_key = LS(left_key, shift_table[round_count])
        right_key = LS(right_key, shift_table[round_count])

        k = left_key + right_key
        round_keys.append("".join(k[i - 1] for i in key_comp))

    return round_keys


def get_round_keys_decrypt(key):
    round_keys = []

    # PC-1
    key = "".join(key[i - 1] for i in keyp)

    # C0
    left_key = key[:28]
    # D0
    right_key = key[28:]
    for round_count in range(15, -1, -1):
        k = left_key + right_key
        round_keys.append("".join(k[i - 1] for i in key_comp))

        left_key = RS(left_key, shift_table[round_count])
        right_key = RS(right_key, shift_table[round_count])
    return round_keys


def Expansion(binary):
    return "".join([binary[i - 1] for i in exp_d])


def Permutation(binary):
    return "".join([binary[i - 1] for i in per])


def S(binary):
    inputs = [binary[i : i + 6] for i in range(0, 48, 6)]
    coords = [(bin2dec(x[0] + x[-1]), bin2dec(x[1:-1])) for x in inputs]
    outputs = [dec2bin(sbox[i][x[0]][x[1]]) for i, x in enumerate(coords)]
    return "".join(outputs)


def F(right, k):
    tmp = Expansion(right)
    tmp = xor(tmp, k)
    tmp = S(tmp)
    tmp = Permutation(tmp)
    return tmp


def encrypt(pt, key):
    assert len(pt) == 64

    pt = "".join([pt[i - 1] for i in initial_perm])
    left_pt = pt[0:32]
    right_pt = pt[32:]

    for k in get_round_key_encrypt(key):
        left_pt, right_pt = right_pt, xor(left_pt, F(right_pt, k))

    combined = right_pt + left_pt
    combined = "".join([combined[i - 1] for i in final_perm])
    return combined


def decrypt(ct, key):
    assert len(ct) == 64

    ct = "".join([ct[i - 1] for i in initial_perm])
    left_pt = ct[0:32]
    right_pt = ct[32:]

    for k in get_round_keys_decrypt(key):
        left_pt, right_pt = right_pt, xor(left_pt, F(right_pt, k))

    combined = right_pt + left_pt
    combined = "".join([combined[i - 1] for i in final_perm])
    return combined


def triple_des_encrypt(pt, key1, key2, key3):
    # if not key1 == key2 and not key3 == key2:/
    ct = encrypt(pt, key1)
    ct = decrypt(ct, key2)
    ct = encrypt(ct, key3)
    return ct


def triple_des_decrypt(ct, key1, key2, key3):
    # if not key1 == key2 and not key3 == key2:/
    pt = decrypt(ct, key3)
    pt = encrypt(pt, key2)
    pt = decrypt(pt, key1)
    return pt

from das.algorithms.convert import encode, decode
def main():
    pt = encode('hello')
    print("Binary Plain Text")
    print(pt)
    key1 = hex2bin("A00000200F000000")
    key2 = hex2bin("A00000100F000000")
    key3 = hex2bin("A00000000B000000")

    ct = [triple_des_encrypt(b, key1, key2, key3) for b in pt]
    print("Binary Cipher Text")
    print(ct)

    text_to_send = decode(ct)
    print("String Cipher Text")
    print(text_to_send)

    ct_bin = encode(text_to_send)
    print("Binary Cipher Text (decoded from String CT")
    print(ct_bin)

    pt_bin = [triple_des_decrypt(b, key1, key2, key3) for b in ct_bin]
    print("Binary Plain Text (decrypted)")
    print(pt_bin)

    pt = decode(pt_bin)
    print("String Plain Text (decrypted)")
    print(pt)

if __name__ == "__main__":
    main()

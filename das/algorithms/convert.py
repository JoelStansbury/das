# import triple_DES

def encode(string, block_size=64):
    bin = ''.join(f"{ord(x):08b}" for x in string)
    if len(bin) % block_size:
        rem = block_size * (1 + len(bin) // block_size) - len(bin)
        bin += '0'*rem
    return [bin[i:i+block_size] for i in range(0, len(bin), block_size)]


def decode(blocks):
    string = "".join(blocks)
    bytes = [string[i:i+8] for i in range(0, len(string), 8)]
    return "".join(chr(int(b,2)) for b in bytes if int(b,2) !=0 )


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


def compress(bin_blocks):
    return " ".join([bin2hex(s) for s in bin_blocks])

def decompress(hex_block_str):
    hex_blocks = hex_block_str.split()
    return [hex2bin(s) for s in hex_blocks]

if __name__ == "__main__":
    pt = "This is just a test."
    blocks = encode(pt)

    assert all([len(b) == 64 for b in blocks])
    print("\nPlaintext Blocks:", blocks)
    print("\nPlaintext:", decode(blocks))
    print()

    print(compress(blocks))
    print(decode(decompress(compress(blocks))))

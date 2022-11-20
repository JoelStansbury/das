
def encode(string, block_size=64):
    bin = ''.join(f"{ord(x):08b}" for x in string)
    rem = len(bin) % block_size
    bin += '0'*rem
    return [bin[i:i+block_size] for i in range(0, len(bin), block_size)]


def decode(blocks):
    string = "".join(blocks)
    bytes = [string[i:i+8] for i in range(0, len(string), 8)]
    return "".join(chr(int(b,2)) for b in bytes)


if __name__ == "__main__":
    pt = "This is just a test."
    blocks = encode(pt)

    assert all([len(b) == 64 for b in blocks])
    print("\nPlaintext Blocks:", blocks)
    print("\nPlaintext:", decode(blocks))
    print()


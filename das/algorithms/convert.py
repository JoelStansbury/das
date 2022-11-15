
def str2ints(s):
    return [ord(c) for c in s]

def ints2str(ints):
    h = ints2hex(ints)
    return "".join([chr(i) for i in hex2ints(h, bpi=2)])

def ints2hex(ints):
    return "0x" + "".join(hex(i)[2:] for i in ints)

def str2hex(s):
    return "0x"+"".join(hex(i)[2:] for i in str2ints(s))

def hex2ints(h, bpi=2):
    """
    bpi: (bytes_per_int)
        This parameter governs how large the integers are.
        For encryption it may be necessary to use bytes_per_int > 2.
        For converting back to a string, bpi must be 2 (2 bytes per char)
    """
    h = h.strip("0x")
    return [int(h[i:i+bpi], base=16) for i in range(0,len(h),bpi)]

def hex2str(h):
    return "".join(chr(i) for i in hex2ints(h))

def encode(string, bpi=16):
    return hex2ints(str2hex(string), bpi)

def decode(ints):
    return ints2str(ints)

if __name__ == "__main__":
    pt = "This is just a test."
    print("\nPlaintext String:", pt)

    blocks = encode(pt)
    print("Plaintext INTS:", blocks)

    blocks[0] += 10**18
    
    print("\nCiphertext INTS:", blocks)
    print("Ciphertext:", decode(blocks))

    blocks[0] -= 10**18
    print("\nPlaintext:", decode(blocks))
    print()
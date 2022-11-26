from .util import Algorithms, mod
from .primes import large_prime

class RSA:
    def __init__(self, p=None, q=None):
        self.p = p or large_prime()
        self.q = q or large_prime()
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)

        self.k = 1
        for k in range(2, self.phi_n):  # 1 < k < phi_n
            if Algorithms.gcd(k, self.phi_n) == 1:
                self.k = k
                break
        self.d = mod(self.phi_n).inverse(self.k)

    def encrypt(self, message):
        """
        Safely computes message**k%n
        """
        print("RSA ENCRYPT")
        return mod(self.n).exp(message, self.k)

    def decrypt(self, ciphertext):
        """
        Safely computes ciphertext**d%n
        """
        return mod(self.n).exp(ciphertext, self.d)

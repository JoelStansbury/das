import random

from .util import Algorithms, mod

LARGE_PRIMES = list(Algorithms.prime_sieve(1000))


class RSA:
    def __init__(self, p=None, q=None):
        self.p = p or random.choice(LARGE_PRIMES)
        self.q = q or random.choice(LARGE_PRIMES)
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)

        for k in range(2, self.phi_n):  # 1 < k < phi_n
            if Algorithms.gcd(k, self.phi_n) == 1:
                self.k = k
                break
        self.d = mod(self.phi_n).inverse(self.k)

    def encrypt(self, message):
        """
        Safely computes message**k%n using the multiplicative property
        of modulo arithmatic... (ab)%n = (a%n)(b%n)%n
        Could be optimized further (to be logarithmic wrt k)
        """
        ciphertext = 1
        for i in range(self.k):
            ciphertext = ciphertext * message % self.n
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Safely computes ciphertext**d%n using the multiplicative property
        of modulo arithmatic... (ab)%n = (a%n)(b%n)%n
        Could be optimized further (to be logarithmic wrt d)
        """
        message = 1
        for i in range(self.d):
            message = message * ciphertext % self.n
        return message

import random

from util import Algorithms, mod

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
        ciphertext = 1
        for i in range(self.k):
            ciphertext = ciphertext * message % self.n
        return ciphertext

    def decrypt(self, ciphertext):
        message = 1
        for i in range(self.d):
            message = message * ciphertext % self.n
        return message


if __name__ == "__main__":
    r = RSA(79, 89)

    print(f"k = {r.k} (should be 5)")
    print(f"d = {r.d} (should be 1373)")
    print(f"d = {r.n} (should be 7031)")

    assert (
        r.encrypt(44) == 4119
    ), "Does not match example (p=79, q=89, ciphertext=4119). NOT {r.encrypt(44)}"
    assert r.d * r.k % r.phi_n == 1, "d and k are not inverses!"
    assert r.decrypt(r.encrypt(100)) == 100, r.decrypt(r.encrypt(100))

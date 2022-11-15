import math
from random import randrange
from decimal import Decimal


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def rand_prime():
    while True:
        p = randrange((10 ** 17), (10 ** 18), 2)
        if all(p % n != 0 for n in range(3, int(p ** 0.5), 2)):
            return p


p = rand_prime()
q = rand_prime()
e = 0
k = 10 ** 17

n = p * q
phi_n = (p - 1) * (q - 1)

for k in range(2, phi_n):
    if gcd(k, phi_n) == 1:
        e = k
        break


def encrypt(me):
    en = math.pow(me, e)
    c = en % n
    print("Encrypted Message is: ", c)
    return c

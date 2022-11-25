from random import randint
from sympy import nextprime

lower_bound = 2**128
def large_prime():
    x = randint(1, 100)
    return nextprime(lower_bound, x)

if __name__ == "__main__":
    print(large_prime())
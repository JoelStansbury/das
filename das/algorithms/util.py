from random import randint

class Algorithms:
    def prime_sieve(n):
        A = [1 for i in range(n)]
        for i in range(2, int(n**0.5)+1):
            if A[i]:
                yield i
                for j in range(i**2, n, i):
                    A[j] = 0
        i+=1
        while i<n:
            if A[i]: yield i
            i+=1
    
    def gcd(a, b, verbose=False):
        """Greatest Common Divisor (Euclidian Alg)
        largest integer that divides both a and b
        """
        # Ensure a is the larger value
        b, a = sorted([abs(a), abs(b)])
        r = a % b
        while r > 0:
            if verbose: print(f"{a} = {a // b} x {b} + {r}")
            a = b
            b = r
            r = a % b
        return b

    def rel_prime(a,b):
        return Algorithms.gcd(a,b) == 1

    def miller_rabin(n):
        """Numerical method for testing primeness.
        In order to be practical, this would need to be altered
        to test many random integers (a).
        """
        # find ints k>0 and q (odd) such that (n-1)=(2**k)q
        tmp = n-1
        k=0
        while tmp%2==0:
            k+=1
            tmp/=2
        q = (n-1)//(2**k)
        a = randint(2,n-2)
        if (a**q)%n == n-1:
            return "inconclusive"
        for j in range(0,k):
            if (a**(2*j*q))%n == n-1:
                return "inconclusive"
        return "composite"

class mod:
    def __init__(self, n):
        self.n = n
    
    def exp(self, a, e):
        """
        Compute a^p mod(n)
        Usage
        -----
        >>>> mod(n=5).exp(a=3, e=5)
        """
        r = 1
        # Convert the exponent (e) into binary
        # bin(__number: int) is a builtin python function which returns
        # the binary repr of its argument.
        bits = bin(e).strip("0b")
        # For each bit in the binary string
        for bit in bits:
        # If bit is a "1", square and multiply
            if bit == "1":
                r = (r**2) * a
            # If bit is a "0", square
            else:
                r = r**2
            # Apply the mod after each operation. This could also be
            # done after the loop, but keeping r as small as possible
            # makes the operations faster.
            r = r % self.n
        return r

    def congruent(self, a, b):
        return a%self.n == b%self.n
    
    def add(self, a, b):
        return (a+b)%self.n
    
    def subtract(self, a, b):
        return (a-b)%self.n

    def inverse(self, x, verbose=False):
        """ Extended Euclidean Algorithm """

        n = self.n
        v = verbose

        # If x and n are not relatively prime
        # then there is no inverse
        if Algorithms.gcd(x, n) != 1: return None

        P = [0, 1]
        Q = []
        
        # To determine each quotient q we use the following formula
        # a = q(b) + r
        # where a and b are initialized as follows
        a = n
        b = x

        def log(i, q_calc=None, p_calc=None):
            prefix = f"Step {i}: "
            q_calc = q_calc or f"{n} = {a//b}({a}) + {a%b}"
            sep = f"{' '*(30-len(prefix+q_calc))}P[{i}] = "
            p_calc = p_calc or f"({P[-3]} - {P[-2]}*{Q[-3]}) % {n} = {P[-1]}"
            print(prefix+q_calc+sep+p_calc)

        # q and r are determined algebraically
        # q -> a // b (and is stored in Q for use later on)
        # r -> a % b
        # a -> b
        # b -> r
        # Or equivalently ...
        Q.append(a // b)
        if v: log(0, p_calc="0")
        a, b = b, a % b

        Q.append(a // b)
        if v: log(1, p_calc="1")
        a, b = b, a % b

        # "For the remainder of the steps, we recursively calculate 
        # ????[i] = ????[i-2] ??? ????[i-1] ????[i-2] mod ????. Continue this
        # calculation for one step beyond the last step of 
        # the Euclidean algorithm."
        # - Dr. Xinyue Zhang (Lecture 3, Slide 12 )
        i=1
        while b!=0:
            P.append((P[-2] - P[-1]*Q[-2]) % n)
            Q.append(a // b)
            if v: log(i:=i+1)
            a, b = b, a % b

        P.append((P[-2] - P[-1]*Q[-2]) % n)
        Q.append(None)
        if v: log(i+1, q_calc=" "*10)
        
        return P[-1]

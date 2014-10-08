import unittest
import random

def gcd(a, b):
    if b > 0:
        return gcd(b, a % b)
    else:
        return a

def gen_primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

def power(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power(x*x, n/2)
    else:
        return x * power(x*x, (n - 1)/2)

def modular_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

class Key(object):
    def __init__(self):
        # List of prime numbers
        primes = []
        for n in gen_primes():
            primes.append(n)
            if len(primes) == 1000:
                break

        # Choosing e - public key exponent
        while True:
            p = random.choice(primes[100:])
            q = random.choice(primes[100:])
            n = p * q
            fi = (p - 1) * (q - 1) # totient of n

            for e in primes[:50]:
                if 1 < e and e < fi and gcd(e, fi) == 1:
                    break
            else:
                continue
            break

        # Calculating d - private key exponent:
        d = 1
        while True:
            if ((d * e) % fi) == 1:
                break
            else:
                d += 1

        self.public = (n, e)
        self.private = (n, d)

class Coder(object):
    def __init__(self, public_key):
        self.n, self.e = public_key

    def code(self, data):
        #return (data ** self.e) % self.n
        #return (power(data, self.e)) % self.n
        return modular_pow(data, self.e, self.n)

class Decoder(object):
    def __init__(self, private_key):
        self.n, self.d = private_key

    def decode(self, data):
        #return (data ** self.d) % self.n
        #return (power(data, self.d)) % self.n
        return modular_pow(data, self.d, self.n)

class test_rsa(unittest.TestCase):
    def test_rsa_basic(self):
        k = Key()

        c = Coder(k.public)
        d = Decoder(k.private)

        self.assertEqual(d.decode(c.code(0)), 0)
        self.assertEqual(d.decode(c.code(1)), 1)
        self.assertEqual(d.decode(c.code(2)), 2)
        self.assertEqual(d.decode(c.code(123)), 123)
        self.assertEqual(d.decode(c.code(1234)), 1234)

if __name__ == "__main__":
    unittest.main()

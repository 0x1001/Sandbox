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

            e = random.choice(primes[:50])

            if 1 < e and e < fi and gcd(e, fi) == 1:
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
        return (data ** self.e) % self.n

class Decoder(object):
    def __init__(self, private_key):
        self.n, self.d = private_key

    def decode(self, data):
        return (data ** self.d) % self.n

class test_rsa(unittest.TestCase):
    def test_key(self):
        k = Key()
        self.assertIsInstance(k.public, tuple)
        self.assertIsInstance(k.private, tuple)

    def test_rsa_basic(self):
        k = Key()

        c = Coder(k.public)
        d = Decoder(k.private)

        self.assertEqual(d.decode(c.code(123)), 123)

if __name__ == "__main__":
    unittest.main()

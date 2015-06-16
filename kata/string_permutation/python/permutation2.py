import unittest


def perm(A, out):
    if len(A) == 0:
        return []

    a = A[0]
    rest = A[1:]

    perms = perm(rest, out)

    new = [a]
    for n in perms:
        for i in range(len(n) + 1):
            new.append(n[:i] + a + n[i:])

    out.extend(new)
    return out


class Test_perm(unittest.TestCase):
    def test_perm_3(self):
        out = []

        perm("abc", out)

        self.assertIn('a', out)
        self.assertIn('b', out)
        self.assertIn('c', out)
        self.assertIn('ab', out)
        self.assertIn('ba', out)
        self.assertIn('ac', out)
        self.assertIn('ca', out)
        self.assertIn('bc', out)
        self.assertIn('cb', out)

        self.assertEqual(len(out), 15)
        self.assertEqual(len(set(out)), 15)

    def test_perm_5(self):
        out = []

        perm("abcde", out)

        self.assertEqual(len(out), 325)
        self.assertEqual(len(set(out)), 325)

if __name__ == "__main__":
    unittest.main()
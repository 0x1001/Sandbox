import unittest


def permute(string):
    list_of_results = []

    _permute(string, '', list_of_results)

    return list_of_results


def _permute(string, result, list_of_results):
    if string == '':
        list_of_results.append(result)
    else:
        for n in string:
            sub_str = string.replace(n, '')
            _permute(sub_str, result + n, list_of_results)


class Test_permutation(unittest.TestCase):
    def test_permutation_1(self):
        perms = permute('a')
        self.assertIn('a', perms)

    def test_permutation_2(self):
        perms = permute('ab')
        self.assertIn('ab', perms)
        self.assertIn('ba', perms)

    def test_permutation_3(self):
        perms = permute('abc')

        self.assertIn('abc', perms)
        self.assertIn('acb', perms)
        self.assertIn('bac', perms)
        self.assertIn('cab', perms)
        self.assertIn('bca', perms)
        self.assertIn('cba', perms)

    def test_permutation_6(self):
        import math

        perms = permute('abcdef')
        self.assertEqual(len(perms), math.factorial(6))

    def test_permutation_20(self):
        import math

        perms = permute('abcdefgh')
        self.assertEqual(len(perms), math.factorial(8))

if __name__ == "__main__":
    unittest.main()
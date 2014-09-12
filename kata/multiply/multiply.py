import unittest

def multiply(a,b):
    if a == [] or b == []:
        return []

    product_array = [0 for i in range(len(a) + len(b) + 1)]

    for idx_b, n_b in enumerate(b):
        for idx_a, n_a in enumerate(a):
            product = n_b * n_a

            idx = 0
            while product != 0:
                idx_p = (len(a) - idx_a - 1) + (len(b) - idx_b - 1) + idx
                unity = product % 10

                while unity != 0:
                    overflow = (product_array[idx_p] + unity) / 10

                    if overflow == 0:
                        product_array[idx_p] = product_array[idx_p] + unity
                    else:
                        product_array[idx_p] = (product_array[idx_p] + unity) % 10

                    unity = overflow
                    idx_p += 1

                idx += 1
                product = product / 10

    for idx in range(len(product_array) - 1, 0, -1):
        if product_array[idx] == 0:
            product_array.pop()
        else:
            break

    product_array.reverse()
    return product_array


class Test_multiply(unittest.TestCase):
    def compose(self,d):
        value = 0

        tens = len(d)
        for digit in d:
            tens -= 1
            value += digit * (10**tens)

        return value

    def decompose(self,d):
        value = []

        while d != 0:
            value.append(d % 10)
            d = d / 10

        value.reverse()
        return value

    def test_multiply_empty(self):
        self.assertEqual(multiply([],[]),[])

    def test_multiply_zero(self):
        self.assertEqual(multiply([0],[0]),[0])

    def test_multiply_one(self):
        self.assertEqual(multiply([1],[1]),[1])

    def test_multiply_one_and_two(self):
        self.assertEqual(multiply([1],[2]),[2])
        self.assertEqual(multiply([2],[1]),[2])

    def test_multiply_nine_and_nine(self):
        self.assertEqual(multiply([9],[9]),[8,1])

    def test_multiply_eight_and_nine(self):
        self.assertEqual(multiply([8],[9]),[7,2])

    def test_multiply_two_digits_with_one(self):
        self.assertEqual(multiply([1,1],[1]),[1,1])

    def test_multiply_two_digits_with_one_higher_value(self):
        self.assertEqual(multiply([9,9],[9]),[8,9,1])
        self.assertEqual(multiply([9,9],[8]),[7,9,2])
        self.assertEqual(multiply([5,5],[7]),[3,8,5])

    def test_multiply_two_digits_with_two(self):
        self.assertEqual(multiply([1,1],[1,1]),[1,2,1])
        self.assertEqual(multiply([9,9],[9,9]),[9,8,0,1])
        self.assertEqual(multiply([4,1],[5,9]),[2,4,1,9])

    def test_multiply_three_digits_with_three(self):
        self.assertEqual(multiply([1,1,1],[1,1,1]),[1,2,3,2,1])
        self.assertEqual(multiply([9,9,9],[9,9,9]),[9,9,8,0,0,1])

    def test_multiply_random_numbers(self):
        import random

        random_a = random.randint(0, 10000)
        random_b = random.randint(0, 10000)

        result = self.compose(multiply(self.decompose(random_a),self.decompose(random_b)))
        self.assertEqual(result, random_a * random_b)

    def test_multiply_random_big_numbers(self):
        import random

        a = [random.randint(0,9) for i in range(1000)]
        b = [random.randint(0,9) for i in range(1000)]
        p = multiply(a,b)

        self.assertEqual(self.compose(p), self.compose(a) * self.compose(b))

if __name__ == "__main__":
    unittest.main()


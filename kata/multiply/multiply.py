import unittest

def multiply(a,b):
    if a == [] or b == []:
        return []
    elif a == [0] or b == [0]:
        return [0]

    a.reverse()
    b.reverse()

    product_array = []
    for idx_a, n_a in enumerate(b):
        for idx_b, n_b in enumerate(a):
            product = n_a * n_b

            idx = 0
            while product != 0:
                unity = product % 10
                idx_p = idx_a + idx_b + idx

                if len(product_array) > idx_p:
                    insert(product_array, idx_p, unity)
                else:
                    product_array.append(unity)

                product = product / 10
                idx += 1

    product_array.reverse()
    return product_array

def insert(product_array,idx,unity):
    while True:
        overflow = (product_array[idx] + unity) / 10

        if overflow == 0:
            product_array[idx] = product_array[idx] + unity
            break
        else:
            product_array[idx] = (product_array[idx] + unity) % 10

            if len(product_array) > idx + 1:
                unity = overflow
            else:
                product_array.append(overflow)
                break

        idx += 1

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

    def test_multiply_big(self):
        import random

        random_a = random.randint(0, 100)
        random_b = random.randint(0, 100)

        result = self.compose(multiply(self.decompose(random_a),self.decompose(random_b)))
        self.assertEqual(result, random_a * random_b)

    def test_insert(self):
        array = [1,2,3,4,5,6]
        insert(array,0,1)
        self.assertEqual(array,[2,2,3,4,5,6])

        array = [9,2,3,4,5,6]
        insert(array,0,1)
        self.assertEqual(array,[0,3,3,4,5,6])

        array = [9,9,9,4,5,6]
        insert(array,0,1)
        self.assertEqual(array,[0,0,0,5,5,6])

        array = [9,9,9,9,9,9]
        insert(array,0,1)
        self.assertEqual(array,[0,0,0,0,0,0,1])

        array = [9,9,9,9,9,9]
        insert(array,3,1)
        self.assertEqual(array,[9,9,9,0,0,0,1])

        array = [9,9,9,9,9,9]
        insert(array,5,1)
        self.assertEqual(array,[9,9,9,9,9,0,1])

if __name__ == "__main__":
    unittest.main()


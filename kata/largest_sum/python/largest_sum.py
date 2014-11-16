import unittest

def largest_sum(A):
    if A == []:
        return 0

    maxsum = 0
    sum = 0

    for i in range(len(A)):
        sum += A[i]

        if sum > maxsum:
            maxsum = sum
        elif sum < 0:
            sum = 0

    return maxsum

def largest_sum(A):
    maxsum = None
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]

        if maxsum is None:
            maxsum = None
        if maxsum < sum:
            maxsum = sum

    return maxsum if maxsum is not None else 0

class Test_largest_sum(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(largest_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(largest_sum([1]), 1)

    def test_negative(self):
        self.assertEqual(largest_sum([-1]), -1)

    def test_5_numbers(self):
        self.assertEqual(largest_sum([5, -9, 6, -2, 3]), 7)

if __name__ == "__main__":
    unittest.main()
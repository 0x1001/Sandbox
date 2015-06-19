import unittest


def largest_sum(A):
    return _largest_sum(A, 0, len(A))


def _largest_sum(A, start, stop):

    if len(A[start:stop]) == 0:
        return 0

    if len(A[start:stop]) == 1:
        return A[start]

    max_1 = A[start]
    max_2 = _largest_sum(A, start + 1, stop)
    max_3 = A[stop - 1]
    max_4 = _largest_sum(A, start, stop - 1)
    max_5 = sum(A[start:stop])

    return max(max_1, max_2, max_3, max_4, max_5)


class Test_largest_sum(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(largest_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(largest_sum([1]), 1)

    def test_negative(self):
        self.assertEqual(largest_sum([-1]), -1)
        self.assertEqual(largest_sum([-100, -1, -1, -3, -5, -100]), -1)

    def test_5_numbers(self):
        self.assertEqual(largest_sum([5, -9, 6, -2, 3]), 7)
        self.assertEqual(largest_sum([-100, 10, 10, -3, -5]), 20)

    def test_large_num(self):
        self.assertEqual(largest_sum([100, -1, -1, -3, -5, 100]), 190)
        self.assertEqual(largest_sum([-100, 10, -1, -3, -5, -100]), 10)


if __name__ == "__main__":
    unittest.main()
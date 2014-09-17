import unittest

def find_shift(A):
    """ Finds shift index in shifted array
        [6, 7, 9, 12, 1, 2, 3, 5]
                   ^
        Sorted array that is shifted by k digits.

        Complexity O(lg(n))
    """
    if A == []:
        return None

    return _find_shift_recurrent(A, 0, len(A), A[0])

def _find_shift_recurrent(A, start, stop, shift_value):
    idx = start + (stop - start)/2

    if idx + 1 >= len(A):
        return idx

    if A[idx] >= shift_value and A[idx + 1] < A[idx]:
        return idx
    elif A[idx] < shift_value:
        return _find_shift_recurrent(A, start, idx, shift_value)
    else:
        return _find_shift_recurrent(A, idx, stop, shift_value)

class Test_find_shift(unittest.TestCase):
    def test_find_shift_empyt(self):
        self.assertEqual(find_shift([]), None)

    def test_find_shift_3(self):
        A = [6, 7, 9, 12, 1, 2, 3, 5]

        k = find_shift(A)

        self.assertEquals(k, 3)

    def test_find_shift_1(self):
        A = [6, 7, 1, 2, 3, 5]

        k = find_shift(A)

        self.assertEquals(k, 1)

    def test_find_shift_7(self):
        A = [6, 7, 9, 12, 14, 15, 16, 17, 1, 2, 3, 5]

        k = find_shift(A)

        self.assertEquals(k, 7)

    def test_find_shift_0(self):
        A = [17, 1, 2, 3, 5, 6, 7, 9, 12, 14, 15, 16]

        k = find_shift(A)

        self.assertEquals(k, 0)

    def test_find_shift_9(self):
        A = [2, 3, 5, 6, 7, 9, 12, 14, 15, 16, 1]

        k = find_shift(A)

        self.assertEquals(k, 9)

    def test_find_shift_doubles_7(self):
        A = [6, 6, 7, 9, 12, 14, 15, 16, 2, 3, 5, 6, 6]

        k = find_shift(A)

        self.assertEquals(k, 7)

if __name__ == "__main__":
    unittest.main()

import unittest

def bubble(array, left, right):
    passes = 0
    while True:
        swap_happend = False
        for j in range(len(array) - 1 - passes):
            if array[j] > array [j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap_happend = True

        passes += 1

        if not swap_happend:
            return array

class Test_bubble(unittest.TestCase):
    def test_sort_empty(self):
        self.assertEqual(bubble([], 0, 0),[])

    def test_sort_one_element(self):
        self.assertEqual(bubble([1], 0, 0),[1])

    def test_sort_two_sorted_elements(self):
        self.assertEqual(bubble([1,2], 0, 1),[1,2])

    def test_sort_two_unsorted_elements(self):
        self.assertEqual(bubble([2,1], 0, 1),[1,2])

    def test_sort_three_unsorted_elements(self):
        self.assertEqual(bubble([2,1,3], 0, 2),[1,2,3])

    def test_sort_three_reverse_elements(self):
        self.assertEqual(bubble([3,2,1], 0, 2),[1,2,3])

    def test_sort_random_numbers(self):
        import random

        random_list = [random.randint(0,1000) for i in range(1000)]
        sorted_list = bubble(random_list[:], 0, len(random_list) - 1)

        random_list.sort()
        self.assertEqual(sorted_list,random_list)

if __name__ == "__main__":
    unittest.main()
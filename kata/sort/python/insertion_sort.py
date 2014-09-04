import unittest

def insertion_sort(list_to_sort):
    for idx_range in range(len(list_to_sort)):
        for idx in range(idx_range,0,-1):
            if list_to_sort[idx - 1] > list_to_sort[idx]:
                list_to_sort[idx - 1],list_to_sort[idx] = list_to_sort[idx],list_to_sort[idx - 1]

    return list_to_sort

class Test_insertion_sort(unittest.TestCase):
    def test_sort_empty(self):
        self.assertEqual(insertion_sort([]),[])

    def test_sort_one_element(self):
        self.assertEqual(insertion_sort([1]),[1])

    def test_sort_two_sorted_elements(self):
        self.assertEqual(insertion_sort([1,2]),[1,2])

    def test_sort_two_unsorted_elements(self):
        self.assertEqual(insertion_sort([2,1]),[1,2])

    def test_sort_three_unsorted_elements(self):
        self.assertEqual(insertion_sort([2,1,3]),[1,2,3])

    def test_sort_three_reverse_elements(self):
        self.assertEqual(insertion_sort([3,2,1]),[1,2,3])

    def test_sort_random_numbers(self):
        import random

        random_list = [random.randint(0,100) for i in range(1000)]
        sorted_list = insertion_sort(random_list[:])

        random_list.sort()
        self.assertEqual(sorted_list,random_list)

if __name__ == "__main__":
    unittest.main()
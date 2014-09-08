import unittest

def qsort(array, left, right):
    if left < right:
        idx = partition(array, left, right)
        qsort(array, left, idx - 1)
        qsort(array, idx + 1, right)

    return array

def partition(array,left,right):
    pivot_index = left + (right - left)/2
    pivot_value = array[pivot_index]
    store_index = left

    array[right], array[pivot_index] = array[pivot_index], array[right]
    for i in range(left,right):
        if array[i] < pivot_value:
            array[i], array[store_index] = array[store_index], array[i]
            store_index += 1

    array[right], array[store_index] = array[store_index], array[right]

    return store_index

class Test_qsort(unittest.TestCase):
    def test_sort_empty(self):
        self.assertEqual(qsort([], 0, 0),[])

    def test_sort_one_element(self):
        self.assertEqual(qsort([1], 0, 0),[1])

    def test_sort_two_sorted_elements(self):
        self.assertEqual(qsort([1,2], 0, 1),[1,2])

    def test_sort_two_unsorted_elements(self):
        self.assertEqual(qsort([2,1], 0, 1),[1,2])

    def test_sort_three_unsorted_elements(self):
        self.assertEqual(qsort([2,1,3], 0, 2),[1,2,3])

    def test_sort_three_reverse_elements(self):
        self.assertEqual(qsort([3,2,1], 0, 2),[1,2,3])

    def test_partition(self):
        array = [5,3,2,6,1,16,10,4]
        partition(array, 0, 7)
        self.assertEqual(array, [5,3,2,4,1,6,10,16])

    def test_sort_random_numbers(self):
        import random

        random_list = [random.randint(0,1000) for i in range(1000)]
        sorted_list = qsort(random_list[:], 0, len(random_list) - 1)

        random_list.sort()
        self.assertEqual(sorted_list,random_list)

if __name__ == "__main__":
    unittest.main()
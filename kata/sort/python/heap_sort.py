import unittest

def heap_sort(array):
    """ Complexity O(n*lg(n)) """
    build_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i - 1)

    return array

def heapify(array, idx, last):
    if array == []:
        return

    left = idx * 2 + 1
    right = idx * 2 + 2

    biggest = idx

    if right <= last:
        if array[idx] <= array[right]:
            biggest = right

    if left <= last:
        if array[biggest] <= array[left]:
            biggest = left

    if biggest != idx:
        array[biggest], array[idx] = array[idx], array[biggest]
        heapify(array, biggest, last)

def build_heap(array):
    for idx in range(len(array)/2 - 1, -1, -1):
        heapify(array, idx, len(array) - 1)

class Test_heap_sort(unittest.TestCase):
    def test_heapify_empty(self):
        array = []
        heapify(array,0,0)
        self.assertEqual(array,[])

    def test_heapify_one(self):
        array = [0]
        heapify(array,0,0)
        self.assertEqual(array,[0])

    def test_heapify_two(self):
        array = [1,2]
        heapify(array,0,1)
        self.assertEqual(array,[2,1])

    def test_heapify_three(self):
        array = [1,2,3]
        heapify(array,0,2)
        self.assertEqual(array,[3,2,1])

    def test_heapify_five(self):
        array = [1,5,6,2,3,4]
        heapify(array,0,5)
        self.assertEqual(array,[6,5,4,2,3,1])

    def test_build_heap(self):
        array = [1,2,3]
        build_heap(array)
        self.assertEqual(array,[3,2,1])

    def test_sort_empty(self):
        self.assertEqual(heap_sort([]),[])

    def test_sort_one_element(self):
        self.assertEqual(heap_sort([1]),[1])

    def test_sort_two_sorted_elements(self):
        self.assertEqual(heap_sort([1,2]),[1,2])

    def test_sort_two_unsorted_elements(self):
        self.assertEqual(heap_sort([2,1]),[1,2])

    def test_sort_three_unsorted_elements(self):
        self.assertEqual(heap_sort([2,1,3]),[1,2,3])

    def test_sort_three_reverse_elements(self):
        self.assertEqual(heap_sort([3,2,1]),[1,2,3])

    def test_sort_ten_elements(self):
        self.assertEqual(heap_sort([5,2,1,4,6,7,10,3,9,8]),[1,2,3,4,5,6,7,8,9,10])

    def test_sort_random_numbers(self):
        import random

        random_list = [random.randint(0,1000) for i in range(10000)]
        sorted_list = heap_sort(random_list[:])

        random_list.sort()
        self.assertEqual(sorted_list,random_list)

if __name__ == "__main__":
    unittest.main()
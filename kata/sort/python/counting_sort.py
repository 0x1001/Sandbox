import unittest

def counting_sort(list_to_sort,max):
    bucket = [ 0 for i in range(max + 1)]

    for e in list_to_sort:
        bucket[e] += 1

    sorted_list = []
    for i, e in enumerate(bucket):
        sorted_list.extend([i]*e)

    return sorted_list

class Test_counting_sort(unittest.TestCase):
    def test_sort_empty(self):
        self.assertEqual(counting_sort([],0),[])

    def test_sort_one_element(self):
        self.assertEqual(counting_sort([1],1),[1])

    def test_sort_two_sorted_elements(self):
        self.assertEqual(counting_sort([1,2],2),[1,2])

    def test_sort_two_unsorted_elements(self):
        self.assertEqual(counting_sort([2,1],2),[1,2])

    def test_sort_three_unsorted_elements(self):
        self.assertEqual(counting_sort([2,1,3],3),[1,2,3])

    def test_sort_three_reverse_elements(self):
        self.assertEqual(counting_sort([3,2,1],3),[1,2,3])

    def test_sort_random_numbers(self):
        import random

        random_list = [random.randint(0,100) for i in range(1000)]
        sorted_list = counting_sort(random_list[:],100)

        random_list.sort()
        self.assertEqual(sorted_list,random_list)

if __name__ == "__main__":
    unittest.main()
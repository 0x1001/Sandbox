import unittest

def merge_sort(list_to_sort):
    if len(list_to_sort) > 1:
        first_half = list_to_sort[:int(len(list_to_sort)/2)]
        second_half = list_to_sort[int(len(list_to_sort)/2):]

        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)

        sorted_list = []
        for idx in range(len(list_to_sort)):
            if len(first_half) == 0:
                sorted_list.extend(second_half)
                break

            if len(second_half) == 0:
                sorted_list.extend(first_half)
                break

            if first_half[0] <= second_half[0]:
                sorted_list.append(first_half.pop(0))
            else:
                sorted_list.append(second_half.pop(0))

        return sorted_list
    else:
        return list_to_sort

class Test_merge_sort(unittest.TestCase):
    def test_sort_empty(self):
        self.assertEqual(merge_sort([]),[])

    def test_sort_one_element(self):
        self.assertEqual(merge_sort([1]),[1])

    def test_sort_two_sorted_elements(self):
        self.assertEqual(merge_sort([1,2]),[1,2])

    def test_sort_two_unsorted_elements(self):
        self.assertEqual(merge_sort([2,1]),[1,2])

    def test_sort_three_unsorted_elements(self):
        self.assertEqual(merge_sort([2,1,3]),[1,2,3])

    def test_sort_three_reverse_elements(self):
        self.assertEqual(merge_sort([3,2,1]),[1,2,3])

    def test_sort_random_numbers(self):
        import random

        random_list = [random.randint(0,100) for i in range(1000)]
        sorted_list = merge_sort(random_list[:])

        random_list.sort()
        self.assertEqual(sorted_list,random_list)

if __name__ == "__main__":
    unittest.main()
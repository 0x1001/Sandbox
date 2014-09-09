import unittest

def binary_search(array,key):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left)/2

        if key == array[mid]:
            return True
        elif key > array[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False

class Test_binary_search(unittest.TestCase):
    def test_empty(self):
        array = []
        key = 0

        self.assertFalse(binary_search(array,key))

    def test_one_item_exists(self):
        array = [0]
        key = 0

        self.assertTrue(binary_search(array,key))

    def test_multiple_items(self):
        max_range = 10000
        array = range(max_range)

        self.assertTrue(binary_search(array,0))
        self.assertTrue(binary_search(array,503))
        self.assertTrue(binary_search(array,223))
        self.assertTrue(binary_search(array,401))
        self.assertTrue(binary_search(array,max_range - 1))
        self.assertFalse(binary_search(array,max_range + 1))

if __name__ == "__main__":
    unittest.main()

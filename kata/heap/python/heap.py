import unittest

def build_max_heap(array):
    for index in range(len(array)/2,len(array)):
        max_heapify(array,index)

    return array

def max_heapify(array,index):
    if index == 0:
        return array
    else:
        if index%2 == 1:
            parent = (index - 1)/2
        else:
            parent = (index - 2)/2

        if array[parent] < array[index]:
            array[parent],array[index] = array[index],array[parent]

        max_heapify(array,parent)

    return array

class Test_heap(unittest.TestCase):
    def test_max_heapify_empty(self):
        self.assertEqual(max_heapify([],0),[])

    def test_max_heapify_one(self):
        self.assertEqual(max_heapify([1],0),[1])

    def test_max_heapify_two(self):
        self.assertEqual(max_heapify([1,2],1),[2,1])

    def test_max_heapify_two_max_heap(self):
        self.assertEqual(max_heapify([2,1],1),[2,1])

    def test_max_heapify_three_max_heap(self):
        self.assertEqual(max_heapify([3,1,2],1),[3,1,2])

    def test_max_heapify_three(self):
        self.assertEqual(max_heapify([2,1,3],2),[3,1,2])

    def test_max_heapify_four_max_heap(self):
        self.assertEqual(max_heapify([4,2,3,1],2),[4,2,3,1])

    def test_max_heapify_four(self):
        self.assertEqual(max_heapify([4,1,3,2],3),[4,2,3,1])

    def test_max_heapify_five(self):
        self.assertEqual(max_heapify([6,3,5,1,2,4,7],6),[7,3,6,1,2,4,5])

    def test_build_max_heap(self):
        self.assertEqual(build_max_heap([4,1,3,2,5]),[5,4,3,1,2])

    def test_build_max_heap_big(self):
        print build_max_heap([1,5,6,7,3,4,15,9,10,11,12])
        self.assertEqual(build_max_heap([1,5,6,7,3,4,15,9,10,11,12]),[15,12,6,9,11,4,1,7,5,3,10])

if __name__ == "__main__":
    unittest.main()
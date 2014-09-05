import unittest
import random

def build_max_heap(array):
    """
        Builds max_heap data structure. O(n*lg(n))
    """
    for index in range(len(array)/2,len(array)): # Half of the array are leafs
        max_heapify(array,index)

    return array

def max_heapify(array,index):
    """
        Fixes one problem in max_heap data structure. Runs bottom up. O(lg(n))
    """
    if index == 0:
        return array
    else:
        if index%2 == 1: # Parrent index is almost two times smaller then child index
            parent = (index - 1)/2
        else:
            parent = (index - 2)/2

        if array[parent] < array[index]:
            array[parent],array[index] = array[index],array[parent]

        max_heapify(array,parent)

    return array

def max_heap(array):
    """
        Returns max value. O(1)
    """
    if len(array) > 0:
        return array[0]
    else:
        return None

def insert_heap(array,element):
    """
        Inserts new element to max_heap data structure. O(lg(n))
    """
    array.append(element)
    max_heapify(array,len(array) - 1)

def delete_heap(array,index):
    """
        Deletes element with given index. O(lg(n))
    """
    child_one = index*2 + 1 # Child index is almost two times bigger then parrent index
    child_two = index*2 + 2

    if child_one >= len(array) and child_two >= len(array): # Index is a leaf (No children)
        array.pop(index)
    elif child_one < len(array) and child_two >= len(array): # One child
        array[child_one], array[index] = array[index], array[child_one]
        array.pop(child_one)
    elif child_one >= len(array) and child_two < len(array): # One child
        array[child_two], array[index] = array[index], array[child_two]
        array.pop(child_two)
    else: # Two children
        if array[child_one] > array[child_two]: # Swap with bigger
            array[child_one], array[index] = array[index], array[child_one]
            delete_heap(array,child_one)
        else:
            array[child_two], array[index] = array[index], array[child_two]
            delete_heap(array,child_two)

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
        self.assertEqual(build_max_heap([1,5,6,7,3,4,15,9,10,11,12]),[15,12,6,9,11,4,1,7,5,3,10])

    def test_max_heap(self):
        array = [random.randint(0,10000) for i in range(100000)]
        build_max_heap(array)
        self.assertEqual(max_heap(array),max(array))

    def test_insert_heap(self):
        array = [random.randint(0,10000) for i in range(100000)]
        build_max_heap(array)
        insert_heap(array,10001)
        self.assertEqual(max_heap(array),10001)

    def test_delete_heap(self):
        array = [random.randint(0,10000) for i in range(100000)]
        build_max_heap(array)
        insert_heap(array,10001)
        delete_heap(array,0)
        self.assertNotEqual(max_heap(array),10001)

if __name__ == "__main__":
    unittest.main()
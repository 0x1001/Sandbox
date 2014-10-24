import unittest

class StackUnderFlow(Exception): pass
class StackOverFlow(Exception): pass

class Stack(object):
    def __init__(self):
        import threading

        self._stack = []
        self._lock = threading.RLock()

    def pop(self):
        with self._lock:
            try:
                return self._stack.pop()
            except IndexError:
                raise StackUnderFlow()

    def push(self,item):
        with self._lock:
            self._stack.append(item)

    def size(self):
        with self._lock:
            return len(self._stack)

    def is_empty(self):
        return True if self.size() == 0 else False

class TowerOfHanoi(object):
    def __init__(self):
        self.t1 = Stack()
        self.t2 = Stack()
        self.t3 = Stack()

    def solve(self, t1_set):
        size = 0
        for element in t1_set:
            self.t1.push(element)
            size += 1

        self._move(self.t1, self.t3, self.t2, size)

        solution = []
        while not self.t3.is_empty():
            solution.append(self.t3.pop())

        return solution

    def _move(self, src, dst, buff, size):
        #self._print()

        if size == 0:
            return
        elif size == 1:
            dst.push(src.pop())
        else:
            self._move(src, buff, dst, size-1)
            self._move(src, dst, buff, 1)
            self._move(buff, dst, src, size-1)

    def _print(self):
        import os
        os.system('cls')

        print self.t1._stack
        print self.t2._stack
        print self.t3._stack

class Test_tower_of_hanoi(unittest.TestCase):
    def test_simple(self):
        solution = TowerOfHanoi().solve([])
        self.assertEqual(solution, [])

    def test_one_element(self):
        solution = TowerOfHanoi().solve([1])
        self.assertEqual(solution, [1])

    def test_two_elements(self):
        solution = TowerOfHanoi().solve([2, 1])
        self.assertEqual(solution, [1, 2])

    def test_three_elements(self):
        solution = TowerOfHanoi().solve([3, 2, 1])
        self.assertEqual(solution, [1, 2, 3])

    def test_ten_elements(self):
        solution = TowerOfHanoi().solve([10, 9, 8,7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(solution, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == "__main__":
    unittest.main()
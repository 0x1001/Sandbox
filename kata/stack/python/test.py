import unittest
import main

class StackTest(unittest.TestCase):
    def setUp(self):
        self._stack = main.Stack()

    def test_pop(self):
        with self.assertRaises(main.StackUnderFlow):
            self._stack.pop()

    def test_push(self):
        self._stack.push(1)

    def test_size(self):
        self.assertEqual(self._stack.size(),0)

    def test_all(self):
        self._stack.push(1)
        self._stack.push(2)
        self._stack.push(3)

        self.assertEqual(self._stack.size(),3)
        self.assertEqual(self._stack.pop(),3)
        self.assertEqual(self._stack.pop(),2)
        self.assertEqual(self._stack.pop(),1)
        self.assertEqual(self._stack.size(),0)

if __name__ == "__main__":
    unittest.main()
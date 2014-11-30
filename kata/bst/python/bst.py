import unittest
import random

class Node(object):
    def __init__(self,key):
        self.root = None
        self.right = None
        self.left = None
        self.key = key

    def __str__(self):
        return str(self.key)

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._node_insert(self.root,key)

    def _node_insert(self,node,key):
        if node.key < key:
            if node.right is None:
                node.right = Node(key)
                node.right.root = node
            else:
                self._node_insert(node.right,key)
        else:
            if node.left is None:
                node.left = Node(key)
                node.left.root = node
            else:
                self._node_insert(node.left,key)

    def find(self,key):
        return False if self._node_find(self.root,key) is None else True

    def min(self):
        return self._node_find_min(self.root).key

    def max(self):
        return self._node_find_max(self.root).key

    def delete(self,key):
        node = self._node_find(self.root,key)

        if node is not None:
            self._node_delete(node)

    def _node_delete(self,node):
        if node.left is not None and node.right is not None:
            successor = self._node_find_max(node.left)
            self._node_swap(node, successor)
            self._node_delete(successor)

        elif node.left is not None:
            if node.root.left is node:
                node.root.left = node.left
            else:
                node.root.right = node.left

            node.left.root = node.root

        elif node.right is not None:
            if node.root.right is node:
                node.root.right = node.right
            else:
                node.root.left = node.right

            node.right.root = node.root

        else:
            if node.root is not None:
                if node is node.root.left:
                    node.root.left = None
                else:
                    node.root.right = None
            else:
                self.root = None

    def _node_swap(self,node_a, node_b):
        node_a.key, node_b.key = node_b.key, node_a.key

    def _node_find(self,node,key):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif node.key < key:
            return self._node_find(node.right,key)
        else:
            return self._node_find(node.left,key)

    def _node_find_max(self,node):
        while node.right is not None:
            node = node.right

        return node

    def _node_find_min(self,node):
        while node.left is not None:
            node = node.left

        return node

    def verify_bst(self):
        if self.root is not None:
            return self._verify_bst(self.root, None, None)
        else:
            return True

    def _verify_bst(self, root, min, max):
        if root is None:
            return True

        if root.left is not None:
            if root.left.key <= root.key:
                if min is None or root.left.key > min:
                    left = self._verify_bst(root.left, min, root.key)
                else:
                    left = False
            else:
                left = False
        else:
            left = True


        if root.right is not None:
            if root.right.key > root.key:
                if max is None or root.right.key <= max:
                    right = self._verify_bst(root.right, root.key, max)
                else:
                    right = False
            else:
                right = False
        else:
            right = True

        return right and left

class Test_BST(unittest.TestCase):
    def balanced_tree(self):
        bst = BST()
        bst.insert(5)
        bst.insert(2)
        bst.insert(7)
        bst.insert(3)
        bst.insert(1)
        bst.insert(6)
        bst.insert(8)

        return bst

    def balanced_tree_with_repeat(self):
        bst = BST()
        bst.insert(5)
        bst.insert(5)
        bst.insert(7)
        bst.insert(3)
        bst.insert(1)
        bst.insert(7)
        bst.insert(8)
        bst.insert(8)

        return bst

    def test_insert_unbalanced_right(self):
        bst = BST()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        self.assertEqual(bst.root.key,1)
        self.assertEqual(bst.root.right.key,2)
        self.assertEqual(bst.root.right.right.key,3)
        self.assertEqual(bst.root.right.right.right.key,4)
        self.assertEqual(bst.root.right.right.right.right.key,5)

    def test_insert_unbalanced_left(self):
        bst = BST()
        bst.insert(5)
        bst.insert(4)
        bst.insert(3)
        bst.insert(2)
        bst.insert(1)

        self.assertEqual(bst.root.key,5)
        self.assertEqual(bst.root.left.key,4)
        self.assertEqual(bst.root.left.left.key,3)
        self.assertEqual(bst.root.left.left.left.key,2)
        self.assertEqual(bst.root.left.left.left.left.key,1)

    def test_insert_balanced(self):
        bst = self.balanced_tree()

        self.assertEqual(bst.root.key,5)
        self.assertEqual(bst.root.left.key,2)
        self.assertEqual(bst.root.right.key,7)
        self.assertEqual(bst.root.left.left.key,1)
        self.assertEqual(bst.root.left.right.key,3)
        self.assertEqual(bst.root.right.left.key,6)
        self.assertEqual(bst.root.right.right.key,8)

    def test_verify_bst(self):
        bst = self.balanced_tree()

        self.assertTrue(bst.verify_bst())

        bst = BST()
        bst.root = Node(10)
        bst.root.left = Node(5)
        bst.root.right = Node(15)
        bst.root.left.left = Node(4)
        bst.root.left.right = Node(6)
        bst.root.left.right.right = Node(11)
        bst.root.right.left = Node(12)
        bst.root.right.right = Node(16)

        self.assertFalse(bst.verify_bst())

    def test_insert(self):
        array = (random.randint(0,10000) for i in range(10000))

        bst = BST()
        map(bst.insert,array)

        self.assertTrue(bst.verify_bst())

    def test_find(self):
        bst = self.balanced_tree()

        self.assertTrue(bst.find(5))
        self.assertTrue(bst.find(2))
        self.assertTrue(bst.find(7))
        self.assertTrue(bst.find(3))
        self.assertTrue(bst.find(1))
        self.assertTrue(bst.find(6))
        self.assertTrue(bst.find(8))
        self.assertFalse(bst.find(9))
        self.assertFalse(bst.find(0))

    def test_min(self):
        array = [random.randint(0,10000) for i in range(100)]

        bst = BST()
        for i in array:
            bst.insert(i)

        self.assertEqual(bst.min(),min(array))

    def test_max(self):
        array = [random.randint(0,10000) for i in range(100)]

        bst = BST()
        for i in array:
            bst.insert(i)

        self.assertEqual(bst.max(),max(array))

    def test_delete_leaves(self):
        bst = self.balanced_tree()

        bst.delete(1)
        self.assertFalse(bst.find(1))

        bst.delete(3)
        self.assertFalse(bst.find(3))

        bst.delete(6)
        self.assertFalse(bst.find(6))

        bst.delete(8)
        self.assertFalse(bst.find(8))

        self.assertTrue(bst.verify_bst())

    def test_delete_node(self):
        bst = self.balanced_tree()
        bst.delete(7)
        self.assertFalse(bst.find(7))
        self.assertTrue(bst.verify_bst())

    def test_delete_multiple(self):
        bst = self.balanced_tree()

        bst.delete(8)
        self.assertFalse(bst.find(8))
        self.assertTrue(bst.verify_bst())

        bst.delete(5)
        self.assertFalse(bst.find(5))
        self.assertTrue(bst.verify_bst())

    def test_delete_with_repeat(self):
        bst = self.balanced_tree_with_repeat()

        self.assertTrue(bst.verify_bst())
        bst.delete(5)
        self.assertTrue(bst.verify_bst())

    def test_integrity(self):
        array = (random.randint(0,10000) for i in range(10000))

        bst = BST()
        map(bst.insert,array)

        self.assertTrue(bst.verify_bst())

        i = 0
        while True:
            i += 1
            r = random.randint(0,10000)
            if bst.find(r) is not Node:
                bst.delete(r)
                self.assertTrue(bst.verify_bst())

            if i == 50:
                break

if __name__ == "__main__":
    unittest.main()
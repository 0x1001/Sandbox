import unittest

class Node(object):
    def __init__(self,key):
        self.root = None
        self.right = None
        self.left = None
        self.key = key

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

    def _node_find(self,node,key):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif node.key < key:
            return self._node_find(node.right,key)
        else:
            return self._node_find(node.left,key)

    def delete(self,key):
        node = self._node_find(self.root,key)

        if node == None:
            return

        self._node_delete(node)

    def _node_delete(self,node):
        if node.left is None and node.right is None:
            if node.root.left is node:
                node.root.left = None
            else:
                node.root.right = None
        elif node.right is None: # Right node is missing so swap with left node
            node.key,node.left.key = node.left.key,node.key
            self._node_delete(node.left)
        else: # Right node is present so swap with right node (doesn't matter if left node is there or not becasue always has to swap with bigger key which is always on right)
            node.key,node.right.key = node.right.key,node.key
            self._node_delete(node.right)

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

    def test_delete(self):
        bst = self.balanced_tree()

        bst.delete(8)
        self.assertFalse(bst.find(8))

        bst.delete(5)
        self.assertFalse(bst.find(5))

        self.assertEqual(bst.root.key,6)
        self.assertEqual(bst.root.left.key,2)
        self.assertEqual(bst.root.left.left.key,1)
        self.assertEqual(bst.root.left.right.key,3)
        self.assertEqual(bst.root.right.key,7)

if __name__ == "__main__":
    unittest.main()
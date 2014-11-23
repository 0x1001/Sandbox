import unittest

class Node(object):
    def __init__(self):
        self.data = None
        self.node1 = None
        self.node2 = None
def transform(root):
    if root is None:
        return root

    begin, end = _transform(root)
    return begin

def _transform(root):
    if root is None:
        return None, None

    left_begin, left_end = _transform(root.node1)
    right_begin, right_end = _transform(root.node2)

    if left_end is not None:
        _merge(left_end, root)

    if right_begin is not None:
        _merge(root, right_begin)

    if left_begin is None:
        left_begin = root

    if right_end is None:
        right_end = root

    return left_begin, right_end

def _merge(a, b):
    b.node1 = a
    a.node2 = b

class Test_linked_list(unittest.TestCase):
    def test_none(self):
        node = transform(None)

        self.assertIsNone(node)

    def test_one(self):
        node = Node()
        node.data = 1

        return_node = transform(node)

        self.assertEqual(return_node, node)

    def test_two(self):
        a = Node()
        a.data = 5

        b = Node()
        b.data = 1

        a.node1 = b

        return_node = transform(a)

        self.assertEqual(return_node.data, 1)
        self.assertEqual(return_node.node2.data, 5)

    def test_multiple(self):
        a = Node()
        a.data = 5

        b = Node()
        b.data = 3

        c = Node()
        c.data = 1

        d = Node()
        d.data = 4

        e = Node()
        e.data = 7

        f = Node()
        f.data = 6

        g = Node()
        g.data = 8


        a.node1 = b
        a.node2 = e

        b.node1 = c
        b.node2 = d

        e.node1 = f
        e.node2 = g

        return_node = transform(a)

        self.assertEqual(return_node.data, 1)
        self.assertEqual(return_node.node2.data, 3)
        self.assertEqual(return_node.node2.node2.data, 4)
        self.assertEqual(return_node.node2.node2.node2.data, 5)
        self.assertEqual(return_node.node2.node2.node2.node2.data, 6)
        self.assertEqual(return_node.node2.node2.node2.node2.node2.data, 7)
        self.assertEqual(return_node.node2.node2.node2.node2.node2.node2.data, 8)


if __name__ == "__main__":
    unittest.main()
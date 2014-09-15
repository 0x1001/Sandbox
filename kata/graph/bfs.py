import unittest

class Vertex(object):
    def __init__(self, name):
        self.neighbors = []
        self.name = name

    def __str__(self):
        return self.name

def bfs(adj):
    visited = []
    for v in adj:
        to_visit = [v]
        while to_visit != []:
            v = to_visit.pop(0)
            if v not in visited:
                visited.append(v)
                for u in v.neighbors:
                    if u not in to_visit:
                        to_visit.append(u)

    return visited

class Test_bfs(unittest.TestCase):
    def test_bfs_empty(self):
        adj = []
        bfs(adj)

    def test_bfs_one(self):
        adj = [Vertex("a")]
        bfs(adj)

    def test_bfs_five(self):
        a = Vertex("a")
        b = Vertex("b")
        c = Vertex("c")
        d = Vertex("d")
        e = Vertex("e")

        a.neighbors = [b, c]
        b.neighbors = [a, e]
        c.neighbors = [b, d, e]
        d.neighbors = [a, e]
        e.neighbors = [b, c]

        adj = [a, b, c, d, e]

        self.assertEqual(bfs(adj), [a, b, c, e, d])

if __name__ == "__main__":
    unittest.main()
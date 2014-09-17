import unittest

class Vertex(object):
    def __init__(self,name):
        self.neighbors = []
        self.name = name

    def __str__(self):
        return self.name

def dfs(adj):
    visited = []
    for v in adj:
        if v not in visited:
            visited.append(v)
            dfs_visit(v,visited)

    return visited

def dfs_visit(vertex,visited):
    for v in vertex.neighbors:
        if v not in visited:
            visited.append(v)
            dfs_visit(v,visited)

class Test_dfs(unittest.TestCase):
    def test_dfs_empty(self):
        adj = []
        dfs(adj)

    def test_dfs_one(self):
        adj = [Vertex("a")]
        dfs(adj)

    def test_dfs_five(self):
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

        self.assertEqual(dfs(adj), [a, b, e, c, d])

if __name__ == "__main__":
    unittest.main()
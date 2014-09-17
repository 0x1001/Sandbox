import unittest
import sys

class Vertex(object):
    def __init__(self,name):
        self.adj = {}               # Dict with neighbors and weigths on edges
        self.name = name            # Optional name
        self.distance = sys.maxint  # Shortest distance is set to infinity
        self.predecessor = None     # Shortes path is not known so the closeset precedessor is not known.

    def weight(self,v):
        return self.adj[v]

    def neighbors(self):
        return self.adj.keys()

    def __str__(self):
        return self.name

def bellman_ford(adj,s):
    s.distance = 0  # Update distance of first vertex

    for i in range(len(adj) - 1):
        for u in adj:
            for v in u.neighbors():
                relax(v,u)

    negative_cycle = []
    for u in adj:
        for v in u.neighbors():
            if v.distance > u.distance + u.weight(v):
                negative_cycle.append((u,v))

    return negative_cycle

def relax(v,u):
    if v.distance > u.distance + u.weight(v):   # Distance at the begining is set to infinity
        v.distance = u.distance + u.weight(v)
        v.predecessor = u

class Test_bellman_ford(unittest.TestCase):
    def test_bellman_ford_one(self):
        s = Vertex("a")
        adj = [s]
        bellman_ford(adj,s)

    def test_bellman_ford(self):
        a = Vertex("a")
        b = Vertex("b")
        c = Vertex("c")
        d = Vertex("d")
        e = Vertex("e")
        f = Vertex("f")

        a.adj = {b: 10, c: 3}
        b.adj = {c: 1, d: 2}
        c.adj = {b: 4,d: 8, e: 2}
        d.adj = {e: 9}
        e.adj = {d: 7}
        f.adj = {a: 7}

        negative_cycle = bellman_ford([a, b, c, d, e], a)

        self.assertEqual(negative_cycle, [])

        self.assertEqual(b.predecessor, c)
        self.assertEqual(c.predecessor, a)
        self.assertEqual(b.distance, 7)
        self.assertEqual(d.predecessor, b)
        self.assertEqual(d.distance, 9)
        self.assertEqual(e.predecessor, c)
        self.assertEqual(e.distance, 5)
        self.assertEqual(f.predecessor, None)
        self.assertEqual(f.distance, sys.maxint)

    def test_bellman_ford_negative(self):
        a = Vertex("a")
        b = Vertex("b")
        c = Vertex("c")
        d = Vertex("d")
        e = Vertex("e")

        a.adj = {b: 10, c: 3}
        b.adj = {c: 1, d: 2}
        c.adj = {b: 4,d: 8, e: 2}
        d.adj = {e: -9}
        e.adj = {d: 7}

        negative_cycle = bellman_ford([a, b, c, d, e], a)

        self.assertEqual(negative_cycle, [(d,e)])

        self.assertEqual(b.predecessor, c)
        self.assertEqual(c.predecessor, a)
        self.assertEqual(b.distance, 7)

if __name__ == "__main__":
    unittest.main()
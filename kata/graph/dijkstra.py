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

def dijkstra(adj,s):
    s.distance = 0  # Update distance of first vertex
    S = set()       # Contains set of verteces that have shortes path calculated. Increases over time
    Q = adj         # List of all vertexes. Decreases over time.

    while Q != []:
        u = extract_min(Q)          # Get vertex with shortes path and remove it from queue
        S.add(u)                    # Addit to S
        for v in u.neighbors():     # Relax all edges
            relax(v,u)

def relax(v,u):
    if v.distance > u.distance + u.weight(v):   # Distance at the begining is set to infinity
        v.distance = u.distance + u.weight(v)
        v.predecessor = u

def extract_min(array):
    smallest = None
    smallest_idx = 0

    for i,distance in enumerate(array):
        if smallest != None or distance < smallest:
            distance = smallest
            smallest_idx = i

    return array.pop(smallest_idx)

class Test_dijkstra(unittest.TestCase):
    def test_dijkstra_one(self):
        s = Vertex("a")
        adj = [s]
        dijkstra(adj,s)

    def test_dijkstra(self):
        a = Vertex("a")
        b = Vertex("b")
        c = Vertex("c")
        d = Vertex("d")
        e = Vertex("e")

        a.adj = {b: 10, c: 3}
        b.adj = {c: 1, d: 2}
        c.adj = {b: 4,d: 8, e: 2}
        d.adj = {e: 9}
        e.adj = {d: 7}

        dijkstra([a, b, c, d, e], a)

        self.assertEqual(b.predecessor, c)
        self.assertEqual(c.predecessor, a)

        self.assertEqual(b.distance, 7)

        self.assertEqual(d.predecessor, c)
        self.assertEqual(d.distance, 11)

        self.assertEqual(e.predecessor, c)
        self.assertEqual(e.distance, 5)

if __name__ == "__main__":
    unittest.main()
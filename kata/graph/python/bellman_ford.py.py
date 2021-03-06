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

    for i in range(len(adj) - 1):       # Repeat |adj| - 1 times
        for u in adj:                   # Relax all edges
            for v in u.neighbors():
                relax(v,u)

    negative_cycle = []
    for u in adj:                                       # Check for negative cycles
        for v in u.neighbors():                         # Check all edges
            if v.distance > u.distance + u.weight(v):   # If any of them can be relaxed that implies negative cycle
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

        a.adj = {b: 10, c: 3}
        b.adj = {c: 1, d: 2}
        c.adj = {b: 4,d: 8, e: 2}
        d.adj = {e: 9}
        e.adj = {d: 7}

        negative_cycle = bellman_ford([a, b, c, d, e], a)

        self.assertEqual(negative_cycle, [])

        self.assertEqual(b.predecessor, c)
        self.assertEqual(c.predecessor, a)
        self.assertEqual(b.distance, 7)
        self.assertEqual(d.predecessor, b)
        self.assertEqual(d.distance, 9)
        self.assertEqual(e.predecessor, c)
        self.assertEqual(e.distance, 5)

    def test_bellman_ford_big(self):
        import random

        adj = [Vertex(str(i)) for i in range(1000)]

        for v in adj:
            for i in range(random.randint(0,10)):
                u = random.choice(adj)
                if u != v:
                    v.adj[u] = random.randint(1,50)

        bellman_ford(adj, adj[0])

##        v = adj[-1]
##        print "Start: " + str(v)
##        while True:
##            print str(v.predecessor) + " - " + str(v.distance)
##
##            if  v.predecessor == adj[0] or v.predecessor is None:
##                break
##            else:
##                v = v.predecessor

if __name__ == "__main__":
    unittest.main()
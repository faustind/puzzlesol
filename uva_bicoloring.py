# In Obedience to the Truth

# UVa 10004

import collections

class EdgeNode:
    def __init__(self):
        self.y = None
        self.weight = None

    def __str__(self):
        return(str(self.y))


class Graph:
    def __init__(self, nvertices, nedges, directed=False):
        self.edges = [None] * nvertices
        self.nvertices = nvertices
        self.nedges = nedges
        self.directed = directed

    def outdegree(self, node):
        return 0 if self.edges[node] is None else len(self.edges[node])

    def show(self):
        """Print the adjacency repr of g."""
        for i in range(self.nvertices):
            print("{}: ".format(i), end=" ")
            if self.edges[i] is None:
                print("\n")
            else:
                print(' '.join(map(str, (ne.y for ne in self.edges[i]))))


def read_graph(g, n, m, directed=False):
    for _ in range(m):
        x, y = map(int, input().split())
        insert_edge(g, x, y, directed)


def insert_edge(g, x, y, directed=False):
    e = EdgeNode()
    e.y = y

    if g.edges[x] is None:
        g.edges[x] = [e]
    else:
        g.edges[x].append(e)

    if not directed:
        insert_edge(g, y, x, True)
# bfs
def bfs(g, start: int):
    """bfs.
    TODO: initialize discovered[], processed[] and parent[]
    """
    def process_vertex_early(v: int):
        pass

    def process_vertex_late(v: int):
        pass

    def process_edge(x, y):
        # pass
        global bipartite
        if color[x] is color[y] :
            bipartite = False
        if color[x] is not None:
            color[y] = not color[x]

    q = collections.deque()

    q.append(start)
    discovered[start] = True

    while q:
        v = q.pop()
        process_vertex_early(v)
        processed[v] = True
        for ne in g.edges[v]:
            y = ne.y
            if (not processed[y]) or g.directed:
                process_edge(v, y)
            if (not discovered[y]):
                q.append(y)
                discovered[y] = True
                parent[y] = v
        process_vertex_late(v)



def two_color(g):
    for i in range(g.nvertices):
        if not discovered[i]:
            color[i] = True
            bfs(g, i)
        if not bipartite:
            return False
    return True

if __name__ == "__main__":
    while True:
        bipartite = True
        n = int(input())
        if n == 0:
            break
        m = int (input())

        g = Graph(n, m)

        read_graph(g, n, m)

        discovered = [False] * g.nvertices
        processed = [False] * g.nvertices
        parent = [-1] * g.nvertices


        color = [None] * g.nvertices
        if two_color(g):
            print('BICOLORABLE.')
        else:
            print('NOT BICOLORABLE.')


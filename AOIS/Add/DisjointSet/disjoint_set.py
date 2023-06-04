from collections import defaultdict


class DisjointSet:
    def _union(self, parent, x, y):
        x_set = self._find(parent, x)
        y_set = self._find(parent, y)

        parent[x_set] = y_set

    def _find(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self._find(parent, parent[i])


class Graph(DisjointSet):
    def __init__(self, size: int) -> None:
        self.size = size
        self.graph = defaultdict(list)

    def add_edge(self, v: int, u: int) -> None:
        self.graph[v].append(u)

    def is_cycle(self):
        parent = [-1] * self.size

        for i in self.graph:
            for j in self.graph[i]:
                x = self._find(parent, i)
                y = self._find(parent, j)
                if x == y:
                    return True

                self._union(parent, x, y)

        
if __name__ == "__main__":
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
     
    if g.is_cycle():
        print ("Graph contains cycle")
    else :
        print("Graph does not contain cycle")

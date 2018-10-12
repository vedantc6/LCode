from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS_iter(self, start):
        stack = [start]
        path = []
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)

            for v in self.graph[vertex]:
                stack.append(v)
        return path

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 5)
    g.addEdge(1, 4)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 1)
    g.addEdge(5, 6)
    g.addEdge(2, 3)
    g.addEdge(3, 7)
    g.addEdge(7, 6)
    g.addEdge(3, 0)

    print("Path is: ", g.DFS_iter(0))

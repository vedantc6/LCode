from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.max_val = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if max(u, v) > self.max_val:
            self.max_val = max(u, v)

    def BFS(self, start):
        V = self.max_val + 1
        queue = []
        visited = [False]*V

        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.pop(0)
            print(start, end = " ")

            for i in self.graph[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print("\n")

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 8)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(7, 9)

    g.BFS(1)

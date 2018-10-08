from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.max_val = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if u > self.max_val:
            self.max_val = u

    def Explore(self, u, visited):
        self.pre[u] = self.cnt
        self.cnt += 1
        visited[u] = True
        print(u, )

        for v in self.graph[u]:
            if visited[v] == False:
                self.Explore(v, visited)

        self.post[u] = self.cnt
        self.cnt += 1

    def DFS(self):
        V = self.max_val + 1
        visited = [False]*V
        self.cnt = 1
        self.pre = [0]*V
        self.post = [0]*V
        count = 0
        for i in range(V):
            if visited[i] == False:
                count += 1
                print("DFS number {}".format(count))
                self.Explore(i, visited)

        print("Node Pre value Post value: ")
        [print(i, self.pre[i], self.post[i]) for i in range(V)]

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

    g.DFS()

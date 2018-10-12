class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def DFS(graph, u):
            for v in graph[u]:
                if v in color:
                    if color[v] != (color[u] + 1) % 2:
                        return False
                else:
                    color[v] = (color[u] + 1) % 2
                    if not DFS(graph, v):
                        return False
            return True

        color = {}
        for u in range(len(graph)):
            if u not in color:
                color[u] = 0
                if not DFS(graph, u):
                    return False
        return True

# Correct but TLE

from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(s, adj_list, visited):
            visited.add(s)

            for d in adj_list[s]:
                if d not in visited:
                    dfs(d, adj_list, visited)

            return visited

        ans = []
        adj_list = defaultdict(list)

        for s, d in connections:
            adj_list[s].append(d)
            adj_list[d].append(s)

        for s, d in connections:
            adj_list[s].remove(d)
            adj_list[d].remove(s)

            if len(dfs(s, adj_list, set())) != n:
                ans.append([s,d])

            adj_list[s].append(d)
            adj_list[d].append(s)

        return ans

# Tarjan's algorithm
from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(s, parent, ans, graph, idn, ids, low, visited):
            visited[s] = True
            idn += 1
            ids[s] = idn
            low[s] = idn

            for d in graph[s]:
                if d == parent:
                    continue

                if not visited[d]:
                    dfs(d, s, ans, graph, idn, ids, low, visited)
                    low[s] = min(low[s], low[d])

                    if ids[s] < low[d]:
                        ans.append([s,d])
                else:
                    low[s] = min(low[s], ids[d])

        def findSCC(n, graph):
            ids = [0 for _ in range(n)]
            low = [0 for _ in range(n)]
            visited = [False for _ in range(n)]
            idn = 0
            ans = []

            for i in range(n):
                if not visited[i]:
                    dfs(i, -1, ans, graph, idn, ids, low, visited)

            return ans

        adj_list = defaultdict(list)

        for s, d in connections:
            adj_list[s].append(d)
            adj_list[d].append(s)

        return findSCC(n, adj_list)

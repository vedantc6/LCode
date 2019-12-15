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

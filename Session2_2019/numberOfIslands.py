class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def isSafe(i, j, visited):
            return (i >= 0 and j >= 0 and i < n and j < m
                    and visited[i][j] == False and grid[i][j] == '1')

        def dfs(i, j, visited):
            valid = [(1,0), (-1,0), (0,-1), (0,1)]
            visited[i][j] = True
            for k in range(4):
                if isSafe(i+valid[k][0],j+valid[k][1], visited):
                    dfs(i+valid[k][0],j+valid[k][1], visited)
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        visited = [[False for j in range(m)] for i in range(n)]
        count = 0

        for i in range(n):
            for j in range(m):
                if visited[i][j] == False and grid[i][j] == '1':
                    dfs(i, j, visited)
                    count += 1

        return count

            

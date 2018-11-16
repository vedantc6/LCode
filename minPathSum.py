class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        cost = [[0]*n for i in range(m)]
        cost[0][0] = grid[0][0]
        for i in range(1, m):
            cost[i][0] = cost[i-1][0] + grid[i][0]
        for j in range(1, n):
            cost[0][j] = cost[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]

        return cost[m-1][n-1]
        

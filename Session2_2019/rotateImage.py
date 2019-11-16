class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # First find transpose, then reverse row values
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t

        for i in range(n):
            start, end = 0, n-1
            while start < end:
                matrix[i][start], matrix[i][end] = matrix[i][end],  matrix[i][start]
                start += 1
                end -= 1
        

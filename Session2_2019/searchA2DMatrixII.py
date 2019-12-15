# Brute force - Slow AF (6%)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not target:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True

        return False

# Faster O(nlogm) (26%)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not target:
            return False

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            l, r = 0, n-1
            while l <= r:
                mid = l + (r-l)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

# Fastest O(m+n) (59%)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not target:
            return False

        m = len(matrix)
        n = len(matrix[0])

        row = m-1
        col = 0

        while col < n and row >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1

        return False

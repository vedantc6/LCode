class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        l = []
        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2+1):
                l.append(matrix[r1][c])
            for r in range(r1+1, r2+1):
                l.append(matrix[r][c2])
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1, -1):
                    l.append(matrix[r2][c])
                for r in range(r2, r1, -1):
                    l.append(matrix[r][c1])
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return l

# Faster
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        visited = [[False]*C for _ in range(R)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        ans = []
        for _ in range(R*C):
            ans.append(matrix[r][c])
            visited[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not visited[cr][cc]:
                r, c = cr, cc
            else:
                di = (di+1)%4
                r, c = r + dr[di], c + dc[di]

        return ans
            

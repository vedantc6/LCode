class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neigh in neighbors:
                    r = row + neigh[0]
                    c = col + neigh[1]
                    if (r < rows and r >= 0) and (c < cols and c >= 0):
                        # -1 means earlier it was 1, now it becomes 0
                        # 2 means earlier it was 0, now it becomes 1
                        if board[r][c] in (1, -1):
                            live_neighbors += 1

                # rule 1 and 3
                if (live_neighbors < 2 or live_neighbors > 3) and board[row][col] == 1:
                    board[row][col] = -1
                # rule 2
                if live_neighbors in (2, 3) and board[row][col] == 1:
                    board[row][col] = 1
                # rule 4
                if live_neighbors == 3 and board[row][col] == 0:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        E = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    E[i][j] = j
                elif j == 0:
                    E[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    E[i][j] = E[i-1][j-1]
                else:
                    E[i][j] = min(E[i-1][j], E[i][j-1], E[i-1][j-1]) + 1
        return E[m][n]


        

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backTrack(s = '', l = 0, r = 0):
            if len(s) == 2*n:
                ans.append(s)
                return
            if l < n:
                backTrack(s + '(', l+1, r)
            if r < l:
                backTrack(s + ')', l, r+1)

        ans = []
        backTrack()
        return ans
        

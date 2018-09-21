class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_len = 0
        visited = {}
        for end in range(len(s)):
            if s[end] in visited:
                start = max(start, visited[s[end]] + 1)
            visited[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len
        

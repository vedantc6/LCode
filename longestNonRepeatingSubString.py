class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        word = ""
        for c in s:
            if c in word:
                max_len = max(len(word), max_len)
            word = word[(word.find(c)+1):] + c

        max_len = max(len(word), max_len)
        return max_len
#         n = len(s)
#         numChars = 128
#         cur_len = max_len = 0
#         prev_index = 0
#         visited = [-1]*numChars
#         visited[ord(s[0])] = 0
#         for i in range(n):
#             prev_index = visited[ord(s[i])]

#             if prev_index == -1 or (i - cur_len > prev_index):
#                 cur_len += 1
#             else:
#                 if cur_len > max_len:
#                     max_len = cur_len
#                 cur_len = i - prev_index

#             visited[ord(s[i])] = i

#         if cur_len > max_len:
#             max_len = cur_len

#         return max_len

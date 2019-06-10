# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Split from middle and exchange the positions of first and last, second and second last elements and so on, till you reach midpoint.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return None
        i = 0
        while i < int(len(s)/2):
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp
            i += 1

        return s

# RECURSIVE
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])

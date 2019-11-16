class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_s = [0]*26
        count_t = [0]*26
        for c, r in zip(s, t):
            count_s[ord(c)-ord('a')] += 1
            count_t[ord(r)-ord('a')] += 1

        return count_s == count_t

# One counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1

        for c in count:
            if c != 0:
                return False
        return True
        

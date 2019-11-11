# Recursive solution (TLE)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def util(s, wordDict):
            if s == "":
                return True
            for i in range(1, len(s)+1):
                if str(s[:i]) in wordDict and util(s[i:], wordDict):
                    # print(s[:i], s[i:])
                    return True
            return False

        d = {}
        for word in wordDict:
            if word not in d:
                d[word] = 1
        return util(s, d)

# Memoization (Accepted, 14%)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def util(s, wordDict, wordbreaks):
            if s == "":
                return True

            if s in wordbreaks:
                return wordbreaks[str(s)]

            for i in range(1, len(s)+1):
                if str(s[:i]) in wordDict and util(s[i:], wordDict, wordbreaks):
                    # print(s[:i], s[i:])
                    wordbreaks[str(s[i:])] = True
                    return True
            wordbreaks[str(s)] = False
            return False

        d = {}
        wordbreaks = {}
        for word in wordDict:
            if word not in d:
                d[word] = 1

        return util(s, d, wordbreaks)

# DP (80%)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n  = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for w in wordDict:
                if dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True
        return dp[-1]

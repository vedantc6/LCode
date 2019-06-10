class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        s = "11"
        for i in range(3, n + 1):
            s += "*"
            len_str = len(s)
            count = 1
            tmp = ""
            for j in range(1, len_str):
                if s[j] != s[j-1]:
                    tmp += str(count + 0)
                    tmp += s[j-1]
                    count = 1
                else: count += 1
            s = tmp
        return s

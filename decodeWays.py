class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.startswith('0'):
            return 0
        n = len(s)
        count = [0]*(n+1)
        count[0] = count[1] = 1

        for i in range(2, n+1):
            count[i] = 0
            if s[i-1] > '0':
                count[i] = count[i-1]
            if (s[i-2] == '1') or (s[i-2] == '2' and s[i-1] < '7'):
                count[i] += count[i-2]
        return count[n]

# Way Faster
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.startswith('0'):
            return 0
        stack = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '0' or s[i-1] > '2':  # only '10', '20' is valid
                    return 0
                stack.append(stack[-2])
            elif 9 < int(s[i-1:i+1]) < 27:         # '01 - 09' is not allowed
                stack.append(stack[-2]+stack[-1])
            else:                                  # other case '01, 09, 27'
                stack.append(stack[-1])
        return stack[-1]
            

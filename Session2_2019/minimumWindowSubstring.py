from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        count_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        char_t = len(count_t)

        # uniques is used to keep track of how many unique characters in t are present in the         # current window in its desired frequency.
        uniques = 0

        l, r = 0, 0
        result = float('inf'), None, None

        # Dictionary which keeps a count of all the unique characters in the current window.
        count_s = {}
        while r < len(s):
            # Add one character from the right to the window
            char = s[r]
            count_s[char] = count_s.get(char, 0) + 1

            # If the frequency of the current character added equals to the desired count in t             # then increment the formed count by 1.
            if char in count_t and count_s[char] == count_t[char]:
                uniques += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and uniques == char_t:
                char = s[l]
                if r - l + 1 < result[0]:
                    result = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a                   # part of the window.
                count_s[char] -= 1
                if char in count_t and count_s[char] < count_t[char]:
                    uniques -= 1

                l += 1

            r += 1

        return "" if result[0] == float('inf') else s[result[1]: result[2] + 1]

# Optimized

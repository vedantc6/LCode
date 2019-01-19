class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res, prev = 0, "I"
        for r in s[::-1]:
            res, prev = res - rom[r] if rom[r] < rom[prev] else res + rom[r], r
        return res
        

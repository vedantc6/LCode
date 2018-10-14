class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 0: i += 1
            else: i += 2
        if i == n - 1: return True
        else: return False
        

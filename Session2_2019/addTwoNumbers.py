class Solution:
    def getSum(self, a: int, b: int) -> int:
        negThresh = 0x80000000
        mask = 0xFFFFFFFF

        while b != 0:
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        return ~(a^mask) if a >= negThresh else a

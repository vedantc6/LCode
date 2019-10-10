class Solution:
    def grayCode(self, n: int) -> List[int]:
        bits = [0]
        for i in range(n):
            bits += [r + pow(2, i) for r in reversed(bits)]
        return bits
        

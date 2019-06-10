class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.res = nums
        for i in range(1, len(self.res)):
            self.res[i] += self.res[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.res[j] - (self.res[i-1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

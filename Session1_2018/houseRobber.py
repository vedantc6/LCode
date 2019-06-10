# Recursive Solution (Top Down)
class Solution:
    def robUtil(self, nums, i):
        if i < 0:
            return 0
        else:
            return max(self.robUtil(nums, i-1), self.robUtil(nums, i-2) + nums[i])

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.robUtil(nums, len(nums)-1)

# Recursion + Memoization
class Solution:
    def robUtil(self, nums, i, l):
        if i < 0:
            return 0
        elif l[i] > -1:
            return l[i]
        else:
            l[i] = max(self.robUtil(nums, i-1, l), self.robUtil(nums, i-2, l) + nums[i])
            return l[i]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [-1]*len(nums)
        return self.robUtil(nums, len(nums)-1, l)

# Dynammic programming
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        mem = [-1]*(n+1)
        mem[0] = 0
        mem[1] = nums[0]
        for i in range(1, n):
            val = nums[i]
            mem[i+1] = max(mem[i], mem[i-1] + val)

        return mem[n]
        

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        res = [1]*n
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]  and res[i] < res[j] + 1:
                    res[i] = res[j] + 1

        return max(res)

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        maxval = max(nums)
        freqs = [0]*(maxval + 1)
        sums = [0]*(maxval + 1)

        for val in nums:
            freqs[val] += 1

        sums[0] = freqs[0]
        sums[1] = freqs[1]

        for i in range(2, maxval+1):
            sums[i] = max(sums[i-2] + freqs[i]*i, sums[i-1])

        return sums[maxval]

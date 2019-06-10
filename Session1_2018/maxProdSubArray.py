class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = minVal = maxProd = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxVal, minVal = minVal, maxVal

            maxVal = max(nums[i], maxVal*nums[i])
            minVal = min(nums[i], minVal*nums[i])

            maxProd = max(maxVal, maxProd)

        return maxProd

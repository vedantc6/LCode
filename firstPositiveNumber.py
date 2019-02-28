class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or max(nums) < 0:
            return 1
        count = 1
        for val in nums:
            if (count in nums) or count == max(nums):
                count += 1
            else:
                return count
        return count
        

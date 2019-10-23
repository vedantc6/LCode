class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            if d[num] > len(nums)//2:
                return num
            else:
                d[num] += 1

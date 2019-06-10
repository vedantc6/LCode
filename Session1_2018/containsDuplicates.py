class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = set(nums)
        if len(nums) != len(res):
            return True
        return False

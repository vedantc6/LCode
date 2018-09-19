class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for index, value in enumerate(nums):
            if target - value in num_dict:
                return [num_dict[target - value], index]
            num_dict[value] = index


        

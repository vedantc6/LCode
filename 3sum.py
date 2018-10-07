class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        nums.sort()
        if len(nums) < 3:
            return l

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i + 1, len(nums) - 1
            
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s == 0:
                    l.append([nums[i], nums[start], nums[end]])
                    start = start + 1
                    end = end - 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif s > 0:
                    end = end - 1
                else:
                    start = start + 1

        return l

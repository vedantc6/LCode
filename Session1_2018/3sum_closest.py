class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # l = []
        closest = 100000000
        res = 0
        nums.sort()
        if len(nums) < 3:
            return l

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i + 1, len(nums) - 1

            while start < end:
                s = nums[i] + nums[start] + nums[end]
                diff = abs(s - target)
                if s == target:
                    return s
                if diff < closest:
                    closest = diff
                    res = s
                if s > target:
                    end = end - 1
                elif s < target:
                    start = start + 1

        return res

class Solution:
    def binarySearch(self, nums, target, left):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi)//2
            if nums[mid] > target or (left and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = self.binarySearch(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        return [left_index, self.binarySearch(nums, target, False)-1]

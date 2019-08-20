class Solution:
    def end_points(self, x, target, left):
        lo = 0
        hi = len(x)

        while lo < hi:
            mid = (lo+hi)//2
            if x[mid] > target or (left and target == x[mid]):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.end_points(nums, target, True)

        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        return [left_index, self.end_points(nums[left_index:], target, False)+left_index-1]

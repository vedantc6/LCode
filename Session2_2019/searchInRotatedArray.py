class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = lo + int((hi-lo)/2)

            if target == nums[mid]:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            if nums[hi] >= nums[mid]:
                if nums[hi] >= target >= nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

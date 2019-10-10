class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minSum = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)
        for i in range(n-2):
            start = i+1
            end = n-1
            while start < end:
                tmp = nums[i] + nums[start] + nums[end]
                if tmp == target:
                    return tmp

                if abs(tmp - target) < abs(minSum - target):
                    minSum = tmp

                if tmp < target:
                    start += 1
                elif tmp > target:
                    end -= 1
        return minSum

# Kadane O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_so_far = max(max_so_far, nums[i])

        return max_so_far

# Greedy O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = max_ending_here = nums[0]
        n = len(nums)

        for i in range(1, n):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

# Divide and Conquer
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def cross_sum(nums, left, right, mid):
            if left == right:
                return nums[left]

            left_sum = float('-inf')
            cur_sum = 0

            for i in range(mid, left-1, -1):
                cur_sum += nums[i]
                left_sum = max(left_sum, cur_sum)

            right_sum = float('-inf')
            cur_sum = 0

            for i in range(mid+1, right+1):
                cur_sum += nums[i]
                right_sum = max(right_sum, cur_sum)

            return left_sum + right_sum

        def helper(nums, left, right):
            if left == right:
                return nums[left]

            mid = left + (right-left)//2

            left_sum = helper(nums, left, mid)
            right_sum = helper(nums, mid+1, right)
            cross = cross_sum(nums, left, right, mid)

            return max(left_sum, right_sum, cross)

        return helper(nums, 0, len(nums)-1)

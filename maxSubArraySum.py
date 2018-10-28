# Recursive Solution
class Solution:
    def maxSubArrayMidUtil(self, a, first, last, mid):
        max_left = -99999
        sum1 = 0
        for i in range(mid, first - 1, -1):
            sum1 += a[i]
            if sum1 > max_left:
                max_left = sum1

        max_right = -99999
        sum1 = 0
        for i in range(mid + 1, last + 1):
            sum1 += a[i]
            if sum1 > max_right:
                max_right = sum1

        return max_left + max_right

    def maxSubArrayUtil(self, a, first, last):
        if first == last:
            return a[first]
        mid = (first + last)//2
        return max(self.maxSubArrayUtil(a, first, mid), self.maxSubArrayUtil(a, mid+1, last), self.maxSubArrayMidUtil(a, first, last, mid))

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        first = 0
        last = len(nums) - 1
        return self.maxSubArrayUtil(nums, first, last)

# TLE (wrong solution)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                tmp_sum = sum(nums[i:j+1])
                if tmp_sum == k:
                    total += 1
        return total

# Cumulative Sum (TLE - maybe because of python)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        n = len(nums)
        cum_sum = [0]*(n+1)
        cum_sum[0] = 0
        for i in range(1, n+1):
            cum_sum[i] = cum_sum[i-1] + nums[i-1]
        for i in range(n):
            for j in range(i+1, n+1):
                tmp_sum = cum_sum[j] - cum_sum[i]
                if tmp_sum == k:
                    total += 1

        return total

# Sum on the go: O(n^2), TLE
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        n = len(nums)

        for i in range(n):
            tmp_sum = 0
            for j in range(i, n):
                tmp_sum += nums[j]
                if tmp_sum == k:
                    total += 1

        return total

# Using hashmap O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        count = 0
        sum1 = 0
        hashmap = {}
        hashmap[0] = 1
        for i in range(n):
            sum1 += nums[i]
            if (sum1 - k) in hashmap:
                count += hashmap[sum1-k]
            if sum1 not in hashmap:
                hashmap[sum1] = 1
            else:
                hashmap[sum1] += 1

        return count

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        d = collections.defaultdict(list)
        result = set()

        for i in range(n-1):
            for j in range(i+1, n):
                d[nums[i] + nums[j]].append((i, j))

        for i in range(n-1):
            for j in range(i+1, n):
                sum1 = target - (nums[i] + nums[j])
                for pair in d[sum1]:
#                     To get unique combinations
                    if i > pair[1]:
                        result.add((nums[pair[0]], nums[pair[1]], nums[i], nums[j]))

        return list(result)
                    

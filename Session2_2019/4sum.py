# Generic N sum solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or nums[0]*N > target or nums[-1]*N < target:
                return

            # 2-sum solution using pointers
            if N == 2:
                s, e = 0, len(nums)-1
                while s < e:
                    tmp = nums[s] + nums[e]
                    if tmp == target:
                        results.append(result + [nums[s], nums[e]])
                        s += 1
                        while s < e and nums[s] == nums[s-1]:
                            s += 1
                    elif tmp < target:
                        s += 1
                    else:
                        e -= 1

            else:
                for i in range(len(nums) - N + 1):
                    if i==0 or (i > 0 and nums[i] != nums[i-1]):
                        nSum(nums[i+1:], target - nums[i], N-1, result + [nums[i]], results)

        results = []
        nums = sorted(nums)
        nSum(nums, target, 4, [], results)
        return results

# Using Three sum
class Solution:
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        nums.sort()
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                while start < end:
                    tmp = nums[start] + nums[end]
                    if tmp == t:
                        l.append([nums[i], nums[start], nums[end]])
                        start = start + 1
                        end = end - 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1

                    elif tmp > t:
                        end = end - 1
                    else:
                        start = start + 1

        return l

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            if i==0 or nums[i] != nums[i-1]:
                threeSumResult = self.threeSum(nums[i+1:], target-nums[i])
                for key in threeSumResult:
                    results.append([nums[i]] + key)
        return results
                

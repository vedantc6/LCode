# Approach 1 - Sorting O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l_streak = 1
        c_streak = 1

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    c_streak += 1
                else:
                    l_streak = max(l_streak, c_streak)
                    c_streak = 1

        return max(l_streak, c_streak)

# Approach 2 - Hash Set + Inteligent Building O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l_streak = 0
        n_set = set(nums)

        for num in n_set:
            if num-1 not in n_set:
                c_num = num
                c_streak = 1

                while c_num + 1 in n_set:
                    c_num += 1
                    c_streak += 1

                l_streak = max(l_streak, c_streak)

        return l_streak

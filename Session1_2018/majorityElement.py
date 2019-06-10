class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # setNum = set(nums)
        # for val in setNum:
        #     if nums.count(val) > len(nums)//2:
        #         return val
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# Another Solution
class Solution:
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)//2]

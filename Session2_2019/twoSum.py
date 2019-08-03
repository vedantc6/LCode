# Two pass O(n) Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i, val in enumerate(nums):
            if val not in sumDict:
                sumDict[val] = i

        for i, val in enumerate(nums):
            if (target - val in sumDict) and sumDict[target - val] != i :
                return [i, sumDict[target - val]]

        return [-1,-1]

# One pass O(n) Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, val in enumerate(nums):
            comp = target - val
            if comp in result:
                return [result[comp], i]
            result[val] = i
        return [-1,-1]
        

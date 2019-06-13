# SLOW
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        singles = []
        for num in nums:
            if num not in singles:
                singles.append(num)
            else:
                singles.remove(num)
        if not singles:
            return 0
        return singles[0]

# FAST
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a ^= num
        return a

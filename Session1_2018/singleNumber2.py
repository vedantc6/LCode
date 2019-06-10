class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashTable = {}
        for num in nums:
            hashTable[num] = 0
        for num in nums:
            if num in hashTable:
                hashTable[num] += 1
        for num in nums:
            if hashTable[num] == 1:
                return num
        

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        num_zeros = 0
        for i in range(n):
            if nums[i] == 0:
                num_zeros += 1
        answer = []
        for i in range(n):
            if nums[i] != 0:
                answer.append(nums[i])
        while num_zeros != 0:
            answer.append(0)
            num_zeros -= 1

        for i in range(n):
            nums[i] = answer[i]

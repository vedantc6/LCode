# Time Complexity: O(n), Space Complexity: O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = 1
        right = 1
        left_prods = [0]*n
        right_prods = [0]*n
        left_prods[0] = 1
        right_prods[n-1] = 1
        output = [0]*n

        for i in range(1, n):
            left_prods[i] = left_prods[i-1]*nums[i-1]

        for i in reversed(range(n-1)):
            right_prods[i] = right_prods[i+1]*nums[i+1]

        for i in range(n):
            output[i] = left_prods[i]*right_prods[i]

        return output

# Time Complexity: O(n), Space Complexity: O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        right = 1
        output = [0]*n
        output[0] = 1

        for i in range(1, n):
            output[i] = output[i-1]*nums[i-1]

        for i in reversed(range(n)):
            output[i] = output[i]*right
            right *= nums[i]

        return output

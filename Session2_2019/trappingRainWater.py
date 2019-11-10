# O(n^2) solution. TLE
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)

        trapped = 0

        for i in range(1, n-1):
            max_left, max_right = max(height[:i]), max(height[i+1:])
            t = max(0, min(max_left, max_right) - height[i])
            trapped += t
            # print(i, t)

        return trapped

# O(n) solution. 2 pass
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)

        trapped = 0
        max_left = [0]*n
        max_right = [0]*n

        max_left[0] = height[0]
        max_right[n-1] = height[n-1]

        for i in range(n):
            max_left[i] = max(max_left[i-1], height[i])

        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        # print(max_left, max_right)
        for i in range(n):
            trapped += max(0, min(max_left[i], max_right[i]) - height[i])

        return trapped

# Using 2 pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trapped = 0
        left = 0
        right = len(height) - 1
        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    trapped += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    trapped += right_max - height[right]
                right -= 1
        return trapped

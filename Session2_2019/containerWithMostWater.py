class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start, end = 0, n-1
        maxArea = 0
        while start < end:
            area = (end - start)*min(height[start], height[end])
            if maxArea < area:
                maxArea = area
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maxArea

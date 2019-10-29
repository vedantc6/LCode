class Compare(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest = "".join(sorted(map(str, nums), key=Compare))
        return '0' if largest[0] == '0' else largest

# Second Solution
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        maxlen = len(str(max(nums))) + 1
        concat = []
        for val in nums:
            tmp = str(val)*maxlen
            concat.append((str(val), tmp[:maxlen]))

        concat = sorted(concat, key = lambda x: x[1], reverse=True)
        str1 = ''
        for val in concat:
            str1 += val[0]
        return '0' if str1[0] == '0' else str1

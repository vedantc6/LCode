class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_count = {}
        for val in nums:
            if val in dict_count:
                dict_count[val] += 1
            else:
                dict_count[val] = 1

        frequency = sorted(list(dict_count.items()), key = lambda x: x[1], reverse=True)
        # print(frequency)
        ans = []
        for i in range(k):
            ans.append(frequency[i][0])
        return ans

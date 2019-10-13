class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dset = {}
        for i in range(len(nums)):
            if nums[i] not in dset:
                dset[nums[i]] = i
            elif (i - dset[nums[i]]) > k:
                dset[nums[i]] = i
            elif (i - dset[nums[i]]) <= k:
                return True
        return False
        

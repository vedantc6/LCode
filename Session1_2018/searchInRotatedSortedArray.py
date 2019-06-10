class Solution:
    def findPivot(self, a, low, high):
        if high < low:
            return -1
        if low == high:
            return low

        mid = int((low + high)/2)
        if mid < high and a[mid] > a[mid+1]:
            return mid
        if mid > low and a[mid] < a[mid-1]:
            return mid-1
        if a[low] >= a[mid]:
            return self.findPivot(a, low, mid-1)
        return self.findPivot(a, mid+1, high)

    def binarySearch(self, a, low, high, target):
        if high < low:
            return -1
        mid = int((low + high)/2)
        if target == a[mid]:
            return mid
        if target > a[mid]:
            return self.binarySearch(a, mid+1, high, target)
        return self.binarySearch(a, low, mid-1, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        n = len(nums)
        pivot = self.findPivot(nums, 0, n-1)
        if pivot == -1:
            return self.binarySearch(nums, 0, n-1, target)
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return self.binarySearch(nums, 0, pivot-1, target)
        return self.binarySearch(nums, pivot+1, n-1, target)

# Different Solution
class Solution:
    def modifiedSearch(self, a, low, high, target):
        if low > high:
            return -1
        mid = int((low + high)/2)
        if a[mid] == target:
            return mid
        if a[mid] >= a[low]:
            if a[low] <= target and target <= a[mid]:
                return self.modifiedSearch(a, low, mid-1, target)
            return self.modifiedSearch(a, mid+1, high, target)
        if a[mid] <= target and target <= a[high]:
            return self.modifiedSearch(a, mid+1, high, target)
        return self.modifiedSearch(a, low, mid-1, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        n = len(nums)
        return self.modifiedSearch(nums, 0, n-1, target)
        

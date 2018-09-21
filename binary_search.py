class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(arr, first, end, target):
            if first <= end:
                mid = first + (end - first)/2
                print(first, end)
                print("Middle value: ", arr[mid])
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    return binary_search(arr, mid + 1, end, target)
                else:
                    return binary_search(arr, first, mid - 1, target)
            else:
                return -1

        return binary_search(nums, 0, len(nums) - 1, target)
        

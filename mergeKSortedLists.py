# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Divide and conquer
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(l1, l2):
            dummy = point = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l2.next
                point = point.next

            point.next = l1 if l1 else l2
            return dummy.next

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge(left, right)

# Heaps
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result, heap = [], []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next

        while heap:
            result.append(heapq.heappop(heap))

        return result

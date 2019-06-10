# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two pass
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0
        while first != None:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while(length > 0):
            length -= 1
            first = first.next

        first.next = first.next.next
        return dummy.next

# One pass
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next

        while first != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

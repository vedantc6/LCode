# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur = None
        while slow:
            nxt = slow.next
            slow.next = cur
            cur = slow
            slow = nxt

        while cur and head:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next

        return True

        

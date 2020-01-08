# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        res = prev = ListNode(0)
        res.next = cur

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and (cur.val == cur.next.val):
                    cur = cur.next
                cur = cur.next
                prev.next = cur
            else:
                prev = prev.next
                cur = cur.next
        return res.next

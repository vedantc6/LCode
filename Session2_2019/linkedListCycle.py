# Hash method
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hash = {}
        while head != None:
            if head in hash:
                return True
            else:
                hash[head] = head.val
            head = head.next
        return False

# 2 pointers (slow and fast)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None) or (head.next is None):
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if (fast is None) or (fast.next is None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True

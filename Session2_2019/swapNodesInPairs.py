# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def util(self, head):
        if head is None or head.next is None:
            return head

        remaining = head.next.next
        newHead = head.next
        head.next.next = head
        head.next = self.util(remaining)

        return newHead

    def swapPairs(self, head: ListNode) -> ListNode:
        return self.util(head)
            

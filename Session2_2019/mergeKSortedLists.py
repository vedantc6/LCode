# Approach 1: Basic
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)

        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        for value in sorted(self.nodes):
            point.next = ListNode(value)
            point = point.next

        return head.next

# Approach 2: Using queue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))

        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return head.next

# Approach 3: Using heapq (optimized approach)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(0)
        while h:
            val, idx = heapq.heappop(h)
            # print(val, idx)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next

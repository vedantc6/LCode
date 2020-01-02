# Recursive Solution
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

This is a DFS approach to copying the values of a linked list. Since, there
are two pointers, we can assume them to be two branches and convert it into
a tree/graph problem. Then, all we have to do is DFS on it to copy all the
nodes. This is a recursive solution.
Takes O(n) time and space
"""
class Solution(object):
    def __init__(self):
        self.hash = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None

        if head in self.hash:
            return self.hash[head]

        node = Node(head.val, None, None)
        self.hash[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

# Iterative Solution
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

Essentially in the iterative solution, we are going through each node and
maintaining a back_up/cloned set of nodes as we encounter:
1. new node: we add it to cloned set
2. already in visited set, then we just refer it
We do this till all the nodes of the linked list are encountered.
This is an iterative solution.
Takes O(n) space and time
"""
class Solution(object):
    def __init__(self):
        self.hash = {}

    def getClonedNode(self, node):
        if node:
            if node in self.hash:
                return self.hash[node]
            else:
                self.hash[node] = Node(node.val, None, None)
                return self.hash[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        old_node = head
        new_node = Node(old_node.val, None, None)
        self.hash[old_node] = new_node

        while old_node != None:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            old_node = old_node.next
            new_node = new_node.next

        return self.hash[head]

# Optimized
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

In this approach, instead of making a dictionary to store visited nodes, we
can add the cloned nodes to the next of their actual nodes.
Takes O(n) time and O(1) space.
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # weaved list creation
        ptr = head
        while ptr:
            # cloned
            new_node = Node(ptr.val, None, None)

            # inserting cloned next to original node
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # link random pointers for cloned nodes created
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # unweave to split into original and cloned nodes list
        ptr_old_list = head
        ptr_cloned_list = head.next
        head_old = head.next

        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_cloned_list.next = ptr_cloned_list.next.next if ptr_cloned_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_cloned_list = ptr_cloned_list.next

        return head_old

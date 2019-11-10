class DLL:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.head = DLL(0, 0)
        self.tail = DLL(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            n = self.d[key]
            self.remove(n)
            self.add(n)
            return self.d[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.remove(self.d[key])
        n = DLL(key, value)
        self.add(n)
        self.d[key] = n
        if len(self.d) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.d[n.key]

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        self.tail.prev = node
        node.next = self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.d[key] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum1 = 0
        for key, val in self.d.items():
            if prefix in key[:len(prefix)]:
                sum1 += val
        return sum1

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = collections.defaultdict(list)
        for word in strs:
            hash[tuple(sorted(word))].append(word)
        return hash.values()

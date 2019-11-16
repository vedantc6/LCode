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

# Another Solution
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = collections.defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            hash[tuple(count)].append(word)
        return hash.values()

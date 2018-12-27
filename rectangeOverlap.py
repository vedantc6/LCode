class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        r1x1, r1y1, r1x2, r1y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        r2x1, r2y1, r2x2, r2y2 = rec2[0], rec2[1], rec2[2], rec2[3]

#         If above another
        if r1y2 <= r2y1 or r1y1 >= r2y2:
            return False
#         If left of another
        if r1x1 >= r2x2 or r1x2 <= r2x1:
            return False
        return True

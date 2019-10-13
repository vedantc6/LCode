class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert_to_minutes(time):
            t = time.split(":")
            return int(t[0])*60 + int(t[1])

        minutes = map(convert_to_minutes, timePoints)
        minutes = sorted(minutes)
        # print(minutes)
        i = 0
        minDiff = minutes[-1]
        n = len(minutes)
        while i <= n:
            diff = abs((minutes[i%n] - minutes[i%n-1])%(24*60))
            if diff < minDiff:
                minDiff = diff
            i += 1
        return minDiff
        

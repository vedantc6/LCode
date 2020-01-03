# Priority Queue
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        free_rooms = []
        intervals = sorted(intervals, key=lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)

# Chronological ordering
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        rooms = 0
        start_list = sorted([i[0] for i in intervals])
        end_list = sorted([i[1] for i in intervals])

        start, end = 0,0
        while start < len(intervals):
            if start_list[start] >= end_list[end]:
                rooms -= 1
                end += 1
            rooms += 1
            start += 1

        return rooms

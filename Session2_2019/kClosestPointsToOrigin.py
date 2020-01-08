class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        pairs = {}
        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            pairs[tuple(point)] = dist

        pairs = sorted(pairs.items(), key=lambda x: x[1])
        result = []
        for pair, value in pairs:
            if len(result) < K:
                result.append(pair)
        return result

# Better sort Solution
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

# O(n) Solution
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            if i >= j:
                return
            k = random.randint(i, j)
            # i is the pivot
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid-1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]

            return j

        sort(0, len(points)-1, K)
        return points[:K]

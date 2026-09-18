class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        if k == len(points):
            return points
        heap = []
        def calcDist(x, y):
            return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        for point in points:
            x, y = point
            cur_dist = -1 * calcDist(x, y)
            if len(heap) < k:
                heapq.heappush(heap, [cur_dist, point])
            elif cur_dist > heap[0][0]:
                heapq.heappushpop(heap, [cur_dist, point])
        ans = []
        for dist, point in heap:
            ans.append(point)
        return ans            




        
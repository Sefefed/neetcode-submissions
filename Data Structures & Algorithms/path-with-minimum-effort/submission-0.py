import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        dist = [[float('inf')] * cols for i in range(rows)]
        heap = [(0, 0, 0)]
        dist[0][0] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            effort, r, c = heapq.heappop(heap)
            if effort > dist[r][c]:
                continue
            if r == rows - 1 and c == cols - 1:
                return effort
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if 0 <= nr < rows and 0 <= nc < cols:
                    edge = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, edge)
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))




                


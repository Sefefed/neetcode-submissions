import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
      adj = [[] for i in range(n + 1)]
      visited = set()
      for u, v, w in times:
        adj[u].append((v, w))
      dist = 0
      heap = [(0, k)] 
      while heap:
        cur_dist, cur_dest = heapq.heappop(heap)
        if cur_dest in visited:
            continue
        dist = max(dist, cur_dist)
        visited.add(cur_dest)
        for v, w in adj[cur_dest]:
            if v not in visited:
                heapq.heappush(heap, (cur_dist + w, v))
      return dist if len(visited) == n else -1          

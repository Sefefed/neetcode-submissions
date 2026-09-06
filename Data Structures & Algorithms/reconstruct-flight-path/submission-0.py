from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        for src in graph:
            graph[src].sort(reverse=True)
        itinerary = []
        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)
            itinerary.append(src)
        dfs("JFK")
        return itinerary[::-1]        









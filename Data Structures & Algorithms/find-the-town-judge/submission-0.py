from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        adj = [[] for i in range(n + 1)]
        for a, b in trust:
            adj[a].append(b)
            trusts[b] += 1
        for i in range(1, n + 1):
            if not adj[i] and trusts[i] == n - 1:
                return i
        return -1           


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            l, h = intervals[i]
            if ans[-1][0] <= l <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], h)
            else:
                ans.append(intervals[i])
        return ans        
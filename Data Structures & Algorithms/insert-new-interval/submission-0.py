class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       intervals.append(newInterval)
       intervals.sort()
       ans = [intervals[0]]
       for i in range(1, len(intervals)):
            start, end = intervals[i]
            if ans[-1][0] <= start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append(intervals[i])    
       return ans        
            

           

        
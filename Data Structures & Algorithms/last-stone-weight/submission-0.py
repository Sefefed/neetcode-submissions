import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1    
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -1 * stones[0]  
            y = -1 * heapq.heappop(stones)  
            x = -1 * heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)
        return 0        

        
            
        
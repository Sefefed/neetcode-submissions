import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_ = 0
        def calcHour(guess):
            time = 0
            for amount in piles:
                reqr = math.ceil(amount / guess)
                time += reqr
            return time <= h
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if calcHour(mid):
                min_ = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_            
                

        
        
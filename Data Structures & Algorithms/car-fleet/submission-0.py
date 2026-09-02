from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        v = defaultdict(int)
        for i in range(len(position)):
          v[position[i]] = speed[i]
        position.sort(reverse=True)  
        fleets = 0
        cur_time = 0
        for pos in position:
            time = (target - pos) / v[pos]
            if time > cur_time:
                fleets += 1
                cur_time = time
        return fleets        





        
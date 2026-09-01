from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)
        for num in bills:
            if num == 10:
                if changes[5] == 0:
                    return False
                else:
                    changes[5] -= 1
            elif num == 20:
                if changes[5] > 0 and changes[10] > 0:
                    changes[5] -= 1
                    changes[10] -= 1    
                elif changes[5] > 2:
                    changes[5] -= 3
                else:
                    return False
            changes[num] += 1
        return True                            



           

        
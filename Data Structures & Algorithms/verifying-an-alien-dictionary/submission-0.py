from collections import defaultdict
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = defaultdict(int)
        for i in range(len(order)):
            rank[order[i]] = i
        def compare(first, second):
            m = max(len(first), len(second))
            for i in range(m):
                if i == len(first):
                    return True
                elif i == len(second):
                    return False    
                elif first[i] == second[i]:
                    continue
                else:
                    if rank[first[i]] > rank[second[i]]:
                        return False
                    else:
                        return True    
            return True        
        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return False
        return True         
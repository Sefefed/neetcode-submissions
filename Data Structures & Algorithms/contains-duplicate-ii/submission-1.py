class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                if i - dict[num] <= k:
                    return True
                dict[num] = i
            else:
                dict[num] = i
        return False                         

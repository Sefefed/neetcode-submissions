class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in dict:
                return [dict[needed], i]
            dict[nums[i]] = i
                
        
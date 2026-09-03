class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        smallest = 0
        running_sum = 0
        max_ = float('-inf')
        for num in nums:
            running_sum += num
            max_ = max(max_, running_sum - smallest)
            smallest = min(running_sum, smallest)
        return max_    


        


        
        
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        def backtrack(i, cur):
            nonlocal ans
            if i == n:
                ans += cur
                return
            backtrack(i + 1, cur)
            backtrack(i + 1, cur ^ nums[i])
        backtrack(0, 0)
        return ans        
        
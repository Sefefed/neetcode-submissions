class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(i, cur):
            if i == n:
                ans.append(cur)
                return
            backtrack(i + 1, cur)
            backtrack(i + 1, cur + [nums[i]])
        backtrack(0, [])       
        return ans 
       

        
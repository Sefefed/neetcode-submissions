class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        def combSum(start, arr, sum_):
            if sum_ > target:
                return
            if sum_ == target:
                ans.append(arr.copy())
                return
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                combSum(i, arr, sum_ + candidates[i])
                arr.pop()
        combSum(0, [], 0)
        return ans
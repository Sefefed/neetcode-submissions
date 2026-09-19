class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []

        def backtrack(start, remaining, arr):
            if remaining == 0:
                ans.append(arr.copy())
                return

            for j in range(start, len(candidates)):

                if j > start and candidates[j] == candidates[j - 1]:
                    continue

                if candidates[j] > remaining:
                    break

                arr.append(candidates[j])

                backtrack(j + 1, remaining - candidates[j], arr)

                arr.pop()

        backtrack(0, target, [])
        return ans
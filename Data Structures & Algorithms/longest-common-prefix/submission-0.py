class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0
        for i in range(len(strs[0])):
            isTrue = True
            letter = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != letter:
                    isTrue = False
                    break
            if not isTrue:
                break
            k += 1
        return strs[0][:k]     

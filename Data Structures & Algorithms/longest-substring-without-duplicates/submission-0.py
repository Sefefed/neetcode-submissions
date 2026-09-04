from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        cnt = defaultdict(int)
        ans = 0
        i = 0
        while i < len(s):
            cur = s[i]
            cnt[cur] += 1
            if cnt[cur] > 1:
                ans = max(ans, i - j)
                while cnt[cur] > 1:
                    cnt[s[j]] -= 1
                    j += 1
            i += 1
        ans = max(ans, i - j)         
        return ans   


        
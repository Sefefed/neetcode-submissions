from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = defaultdict(int)
        l = 0
        max_s = s[0]
        ans = 0
        for r in range(len(s)):
            cnt[s[r]] += 1
            if cnt[s[r]] > cnt[max_s]:
                max_s = s[r]
            if r - l + 1 - cnt[max_s] > k:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)   
        return ans     





          
            


        
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        n = math.gcd(len(str1), len(str2))
        cur = ""
        for i in range(n):
            if str1[i] != str2[i]:
                break
            else:
                cur += str1[i]    
                k = len(cur)
                if cur * (len(str1) // k) == str1 and cur * (len(str2) // k) == str2:
                    ans = cur
        return ans            
        
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = ''
        while n > 0:
            ans += str(n % 2) 
            n //= 2
        return ans.count('1')
        
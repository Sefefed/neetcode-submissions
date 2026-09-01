class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                str += s[i].lower()
        return str == str[::-1]        
        
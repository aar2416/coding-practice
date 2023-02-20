class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        max_length = -1
        output = ""
        for i in range(0, len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and i<j:
                    if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > max_length:
                        max_length = len(s[i:j+1])
                        output = s[i:j+1]
        if output == "":
            output = s[0]
        return output
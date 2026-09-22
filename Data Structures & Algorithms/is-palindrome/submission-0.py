class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for c in s.lower():
            if (c.isalnum()):
                s_new += c
        l = 0
        r = len(s_new) - 1
        while (l < r):
            if s_new[l] != s_new[r]:
                return False
            l += 1
            r -= 1
        return True
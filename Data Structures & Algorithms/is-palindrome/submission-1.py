class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        n = len(s)
        s = s.lower()
        R = []
        for i in range(len(s)):
            if (not(s[i] >=  'a' and s[i] <= 'z') and (not (s[i] >=  '0' and s[i] <= '9'))):
                continue
            R.append(s[i])
        m = len(R)
        for i in range(m // 2):
            if R[i] != R[m - 1 - i]:
                return False
        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def deleting_non_alphanumeric(s: str) -> str:
            new_s = ""
            for c in s:
                if('0' <= c <= '9') or ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
                    new_s += c
            return (new_s)

        def is_palindrom(s: list) -> str:
            s = deleting_non_alphanumeric(s)
            s = s.lower()
            s = list(s)
            left = 0
            right = len(s) - 1
            while (left < right):
                if s[left] != s[right]:
                    return (False)
                left += 1
                right -= 1
            return (True)

        for i in range(len(s)):
            new_s = list(s)
            del new_s[i]
            if (is_palindrom(new_s)):
                return (True)
        return (False)
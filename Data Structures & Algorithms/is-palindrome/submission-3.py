class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s == None):
            return (False)
        elif (s == "") or (len(s) == 1):
            return (True)
        
        def deleting_non_alphanumeric(s: str) -> str:
            new_s = ""
            for c in s:
                if('0' <= c <= '9') or ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
                    new_s += c
            return (new_s)
        
        s = deleting_non_alphanumeric(s)
        s = s.lower()
        s = list(s)
        left = 0
        right = len(s) - 1
        while (left < right):
            if (s[left] == s[right]):
                left += 1
                right -= 1
            else:
                return (False)
        return (True)
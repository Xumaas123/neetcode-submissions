class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        for ch in set(s):
            left = s.find(ch)
            right = s.rfind(ch)
            sub = s[left + 1 :right]
            temp = set(sub)
            count += len(temp)
        return (count)

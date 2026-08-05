class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = list(s)
        T = list(t)
        if len(S) != len(T): 
            return False 
        S.sort()
        T.sort()
        if S == T : 
            return True
        return False
                       
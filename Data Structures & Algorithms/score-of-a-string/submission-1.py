class Solution:
    def scoreOfString(self, s: str) -> int:
        Res = 0 
        n = len(s)
        for i in range(0 , n - 1) : 
            N = ord(s[i + 1]) - ord(s[i])
            print(N)
            if N < 0 : 
                N = - N
                Res += N
            else :
                Res += N
        return Res
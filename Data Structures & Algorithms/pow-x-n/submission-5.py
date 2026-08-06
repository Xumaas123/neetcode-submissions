class Solution:
    def myPow(self, x: float, n: int) -> float:
        S = 1
        if n == 0 :
            return (1)
        if x == 0 :
            return (0)
        if (n < 0):
            n = -n
            while (n > 0):
                S *= x
                n -= 1
            return (1/S)
        else:
            while (n > 0):
                S *= x
                n -= 1
            return (S)        
        
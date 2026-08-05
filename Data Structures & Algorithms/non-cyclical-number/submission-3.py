class Solution:
    def isHappy(self, n: int) -> bool:
        T = set()
        while (1):
            chiffres = list(str(n))
            n = sum([int(i)**2 for i in chiffres])
            if n in T:
                return(False)
            elif(n == 1):
                return(True)
            T.add(n)


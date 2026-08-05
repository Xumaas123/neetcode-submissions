class Solution:
    def isHappy(self, n: int) -> bool:
        def check (n: int) -> int:
            chiffre = [int(c) for c in str(n)]
            S = 0
            for n in chiffre:
                S += n ** 2
                print(S)
            return (S)
        T = set()
        while (1):
            n = check(n)
            if n in T:
                return(False)
            elif(n == 1):
                return(True)
            else:
                T.add(n)


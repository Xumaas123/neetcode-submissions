class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        R = []
        n = len(prices)
        if (len(prices) == 1):
            t = 0
            return t
        for i in range (n - 1):
            for j in range(i+1, n):
                R.append(prices[j] - prices[i])
        t = R[0]
        for i in range(1 , len(R)):
            if R[i] > t  :
                t = R[i]
        if t > 0 :
            return t
        else :
            t = 0 
            return t
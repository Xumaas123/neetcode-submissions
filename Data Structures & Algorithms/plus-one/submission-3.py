class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Sum = 0
        
        for num in digits:
            Sum = Sum * 10 + num
    
        digits = []
        Sum += 1
        while (Sum > 0):
            r = Sum % 10
            Sum //= 10
            digits.append(r)
        digits.reverse()
        return (digits) 
    
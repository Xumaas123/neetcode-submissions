class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        R = []
        for i in s: 
            if i - 1 not in s : 
                count = 1
                t = 1
                while t + i in s : 
                    count += 1 
                    t += 1
                R.append(count)
        if len(R) == 0 : 
            return 0
        B = R[0]
        if len(R) == 1: 
            return B
        for i in range(1,len(R)): 
            if R[i] > B: 
                B =  R[i]
        return B
            

             

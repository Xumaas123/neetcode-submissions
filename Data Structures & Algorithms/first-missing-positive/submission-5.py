class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        t = 1
        n = len(nums) + 1
        for i in range(n) : 
            if t in nums :
                t += 1
            else :
                if t <= 0:
                    t += 1
                else :
                    return t
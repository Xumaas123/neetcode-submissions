class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        R = []
        count = 0
        for i in range(n) : 
            if i == n - 1 and nums[i] == 1:
                count += 1
                R.append(count)
            if nums[i] == 1:
                count += 1
            else : 
                R.append(count)
                count = 0
        return max(R)

    
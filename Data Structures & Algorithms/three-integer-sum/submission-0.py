class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        B = []
        R = []
        if len(nums) < 3  :
            return R
        for i in range(len(nums)-2): 
            for j in range(i + 1, len(nums) - 1) :
                for w in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[w] == 0) :
                        R = [] 
                        R.append(nums[i])
                        R.append(nums[j])
                        R.append(nums[w])
                        R.sort() 
                        if R in B : 
                            continue
                        B.append(R)
        return B
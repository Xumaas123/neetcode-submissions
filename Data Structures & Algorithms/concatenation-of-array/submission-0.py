class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        R = []
        i = 0
        while i < len(nums) : 
            R.append(nums[i])
            i += 1
        i = 0
        while i < len(nums) :
            R.append(nums[i])
            i += 1 
        return R
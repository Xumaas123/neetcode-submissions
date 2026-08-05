class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        while i < n - j :
            if nums[i] == val : 
                nums.remove(nums[i])
                i = 0
                j += 1
                continue
            i += 1
        return len(nums)
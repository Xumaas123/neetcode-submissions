class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        T = set()
        i = 0
        while (i < len(nums)):
            if (nums[i] in T):
                del nums[i]
                k += 1
            else:
                T.add(nums[i])
                i += 1
        return(len(nums))
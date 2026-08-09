class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        fast = slow = 0
        while (fast < len(nums)):
            if (nums[fast] == nums[slow]):
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                k += 1
        return (k + 1)
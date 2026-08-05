class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)) : 
            if nums[i] in count :
                count[nums[i]] += 1
            else : 
                count[nums[i]] = 1
        max_value = None
        max_count = -1
        for i in count:
            if count[i] > max_count : 
                max_value = i
                max_count = count[i]
        return max_value
    
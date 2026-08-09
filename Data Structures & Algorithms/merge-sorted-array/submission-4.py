class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while(nums1[(m + n) - 1 -i] == 0 and j < n):
            nums1[(m + n) - 1 - i] = nums2[j]
            i += 1
            j += 1
        
        nums1.sort()
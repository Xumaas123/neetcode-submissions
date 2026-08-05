class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        right = n - 1
        left = 0
        max_water = 0
        while left < right  :
            width = right - left 
            if heights[left] < heights[right] :
                h = heights[left]
            else : 
                h = heights[right]
            
            water = h * width

            if water > max_water : 
                max_water = water 
            
            if heights[left] < heights[right] : 
                left += 1
            else : 
                right -= 1
        return max_water
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1 
        res = 0
        while left < right:
            if heights[left] >= heights[right]:
                diff= right - left
                res = max(res, heights[right] * diff )
                right -= 1
            elif heights[left] < heights[right]:
                diff= right - left
                res = max(res, heights[left] * diff )
                left += 1
        return res

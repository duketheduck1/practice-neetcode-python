class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        res = 0
        while left < right:
            if heights[left] >=  heights[right]:
                diff  = right - left
                res = max(res, diff * heights[right])
                right -= 1
            elif heights[left] <=  heights[right]:
                diff  = right - left
                res = max(res, diff * heights[left])
                left += 1
        return res
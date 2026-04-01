class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[-1]

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < nums[left]:
                res = min(res, nums[mid])
                right = mid - 1 
            else:
                res = min(res, nums[left])
                left = mid + 1 
        return res
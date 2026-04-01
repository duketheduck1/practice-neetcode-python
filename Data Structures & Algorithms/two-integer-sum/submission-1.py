class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in has:
                return [has[diff],i]
            has[nums[i]] = i

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = {}
        for i in range(len(nums)):
            has[nums[i]] =  1 + has.get(nums[i], 0)
            if has[nums[i]] >= 2:
                return True
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #brute force cant use out of time error
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        hashSet = set()
        for i in range(len(nums)):
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])
        return False
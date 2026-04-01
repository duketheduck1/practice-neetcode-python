class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0
        for n in nums:
            if n!=0:
                prod *= n
            else:
                zero += 1
        
        if zero > 1: return [0]*len(nums)

        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero == 1:
                if c != 0:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod//c

        return res

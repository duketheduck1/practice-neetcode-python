class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        has = {}
        for i in nums:
            has[i] = has.get(i, 0) + 1
            if has[i] > 1:
                return i
        
            
        
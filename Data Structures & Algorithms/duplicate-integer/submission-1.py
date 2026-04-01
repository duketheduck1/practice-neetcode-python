class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1 brute force cant use out of time error
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        #2 hashset method slow af
        # hashSet = set()
        # for i in range(len(nums)):
        #     if nums[i] in hashSet:
        #         return True
        #     hashSet.add(nums[i])
        # return False
        #hashset array
        
        #3 hashmap or dictionary method 
        # dictionary = {}
        # for i in range(len(nums)):
        #     if nums[i] in dictionary:
        #         return True
        #     dictionary[nums[i]] = 1
        # return False
    
        #4 dictionary but using count
        # dict = {}
        # for i in range(len(nums)):
        #     dict[nums[i]]  = 1+ dict.get(nums[i],0)
        #     if dict[nums[i]] > 1:
        #         return True
        # return False

        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False


        
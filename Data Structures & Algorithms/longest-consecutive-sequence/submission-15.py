class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        store = set(nums)
        longest = 0
        for i in store:
           if i - 1 not in store:
            length = 1
            while i + length in store:
                length += 1
            longest = max(longest, length)
        return longest
                
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        i = 0
        res = 0
        for j in range(len(s)):
            while s[j] in c:
                c.remove(s[i])
                i+=1
            c.add(s[j])
            res = max(res, j-i+1)
        return res
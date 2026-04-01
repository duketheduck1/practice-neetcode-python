class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        maxl = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] in string:
                i +=  string.index(s[j]) + 1
            string = s[i:j+1]
            maxl = max(maxl,len(string))
            j+=1
        return maxl
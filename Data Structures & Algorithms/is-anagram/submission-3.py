class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}
        for i in range(len(s)):
            s1[ord(s[i]) - ord("a")] = 1 + s1.get(ord(s[i]) - ord("a"), 0)
            t1[ord(t[i]) - ord("a")] = 1 + t1.get(ord(t[i]) - ord("a"), 0)
        if s1 == t1:
            return True
        return False
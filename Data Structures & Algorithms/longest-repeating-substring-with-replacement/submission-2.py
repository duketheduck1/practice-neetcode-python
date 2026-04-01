class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = 0
        count = {}
        l = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            freq = max(freq, count[s[i]])
            if i - l + 1 - freq > k:
                count[s[l]] -= 1
                l += 1
        return i - l + 1

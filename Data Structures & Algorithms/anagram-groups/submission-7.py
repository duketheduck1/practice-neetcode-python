from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord("a")] += 1
            has[tuple(arr)].append(s)
        return has.values()
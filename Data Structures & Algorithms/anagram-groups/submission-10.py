from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for i in s:
                arr[ord(i)-ord("a")] += 1
            hs[tuple(arr)].append(s)
        return list(hs.values())
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        res = defaultdict(list)
        for i in strs:
            arr = [0]*26
            for c in i:
                arr[ord(c)-ord("a")] += 1
            res[tuple(arr)].append(i)
        return res.values()
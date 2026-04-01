class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def subset(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return 
            if i ==len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            subset(i+1, cur, total + candidates[i])
            cur.pop()
            subset(i+1, cur, total)

        subset(0,[], 0)
        return [list(l) for l in res]
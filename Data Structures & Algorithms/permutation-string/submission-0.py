class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = len(s1)
        count = Counter(s1)
        match = 0
        for i in range(len(s2)):
            if s2[i] in count:
                count[s2[i]] -= 1
                if count[s2[i]] == 0:
                    match += 1
            
            if i>=s and s2[i-s] in count:
                if count[s2[i-s]] == 0:
                    match -= 1
                count[s2[i-s]] += 1
            
            if match == len(count):
                return True
        return False


                
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1 #count number of n 
        freq = [[] for i in range(len(nums)+1)] 
        for key, values in count.items():
            freq[values].append(key) #assign index of freq to count => higher count means later in arr
        #multiple bucket from 0 to n in size since there are n element => the number of bucket is less than or equal to n
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
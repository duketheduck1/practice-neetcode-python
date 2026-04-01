class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        arr = []
        while i < j:
            sum =  numbers[i] + numbers[j] 
            if sum == target:
                arr.append(i+1)
                arr.append(j+1)
                break
            elif sum > target:
                j-=1
            elif sum < target:
                i+=1
        return arr
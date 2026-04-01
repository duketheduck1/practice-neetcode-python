class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = self.merge(nums1, nums2)
        mid = len(arr) // 2
        
        mid = len(arr) // 2
        if len(arr) % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2.0
        return float(arr[mid])

    def merge(self,l1, l2):
        arr = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] > l2[j]:
                arr.append(l2[j])
                j += 1
            else:
                arr.append(l1[i])
                i += 1

        while i < len(l1):
            arr.append(l1[i])
            i+= 1
        while j < len(l2):
            arr.append(l2[j])
            j+= 1
        return arr
        
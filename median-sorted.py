class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = nums1 + nums2
        num3.sort()
        if len(num3) %2 == 0:
            a = len(num3)//2
            return (num3[a-1] + num3[a])/2
        else:
            a = len(num3)//2
            return num3[a]
        
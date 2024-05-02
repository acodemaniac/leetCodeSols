class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        L = nums1 + nums2
        L.sort()
        n = len(L)
        if n % 2 == 0:
            n1,n2 = L[(n - 1) / 2], L[n/2]
            n = n1+n2
            return n/2.0
        else:
            return L[(n-1)/2] 
            

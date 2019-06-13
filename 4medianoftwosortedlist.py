class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l=nums1+nums2
        l=sorted(l)
        if len(l)%2==0:
            return float((l[len(l)/2]+l[len(l)/2-1])/2.0)
        else:
            return float(l[len(l)/2])
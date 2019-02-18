class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        a = set(nums1)
        b = set(nums2)
        return [x for x in a if x in b]

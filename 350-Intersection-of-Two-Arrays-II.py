class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # dicts of each list, where key=integer, value=number of times it occurs
        dict1 = {}
        dict2 = {}
        for i in nums1:
            dict1[i] = nums1.count(i)
        for i in nums2:
            dict2[i] = nums2.count(i)
        
        intersection = []
        for i in dict1:
            for t in range(min(dict1[i], dict2.get(i,0))):
                intersection.append(i)
        return intersection
        

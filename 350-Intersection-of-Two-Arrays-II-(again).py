class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        d1,d2 = {},{}
        for i in nums1:
            d1[i] = d1.get(i,0) + 1
        for j in nums2:
            d2[j] = d2.get(j,0) + 1
        
        results = []
        for e in d1:
            for rep in range(min(d1.get(e,0),d2.get(e,0))):
                results.append(e)
        
        return results

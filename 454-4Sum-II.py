class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        # deal with empty lists
        n = len(A)
        if n == 0: return 0 # no combinations of any kind
        
        # make a dict for each list
        # Keys: elt in the list, Values: number of times elt occurs.
        A_dict,B_dict,C_dict,D_dict = {},{},{},{}
        for i in A:
            A_dict[i] = A_dict.get(i,0)+1
        for i in B:
            B_dict[i] = B_dict.get(i,0)+1
        for i in C:
            C_dict[i] = C_dict.get(i,0)+1
        for i in D:
            D_dict[i] = D_dict.get(i,0)+1
        
        count = 0
        
        # Make dicts of all combinations of dicts A&B, dicts C&D
        ABcombos = {}
        CDcombos = {}
        for i in A_dict:
            for j in B_dict:
                ABcombos[i+j] = ABcombos.get(i+j,0)+(A_dict[i]*B_dict[j])
        for i in C_dict:
            for j in D_dict:
                CDcombos[i+j] = CDcombos.get(i+j,0)+(C_dict[i]*D_dict[j])
        
        # Now we can find working combinations in O(k), where k = len(ABcombos.keys())
        for i in ABcombos:
            if -i in CDcombos:
                count += ABcombos[i]*CDcombos[-i]
        
        # Second try, with dicts:
        # slightly faster, but not enough
        '''
        for aElt in A_dict:
            for bElt in B_dict:
                for cElt in C_dict:
                    diff = -1*(aElt+bElt+cElt)
                    if diff in D_dict:
                        count += (A_dict[aElt]*B_dict[bElt]*C_dict[cElt]*D_dict[diff])
        '''
        
        # First try, with nothing.
        # slow and naive
        '''
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if A[i]+B[j]+C[k]+D[l]==0:
                            count += 1
        '''
        return count
        

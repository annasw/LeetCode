class Solution:
    def numFriendRequests(self, ages: 'List[int]') -> 'int':
        # we're using HASH TABLES
        # which sounds way cooler than dicts
        # i think we can agree
        
        d = {} # for demographics
        
        for p in ages: # for person
            d[p] = d.get(p, 0) + 1
        
        t = 0 # for total
        
        for e in ages: # for element
            for age in range(1,e+1):
                if age > (e/2)+7:
                    t += d.get(age,0)
        
        t -= sum([d.get(x,0) for x in range(15,121)]) # remove the self-requests (which only occur for age>14)
        
        return t
        
        
        # earlier attempt I didn't finish fixing
        # bc i decided to do it the slow, straightforward way to iron out the bugs
        '''for a in range(1, 121): # for age
            for age in range(int(a*.5)+7 + 1, a+1):
                t += d.get(age,0)*d.get(a,1)'''
        
        

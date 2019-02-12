class LRUCache:

    def __init__(self, capacity: 'int'):
        self.lru = {} # actually a dict where values are duples of (value, age-bit)
        self.cap = capacity
        self.age = 0 # running age-bit-tracker
        

    def get(self, key: 'int') -> 'int':

        self.age += 1
        
        if self.cap <= 0: return -1
        
        elt = self.lru.get(key,-1)
        
        if elt == -1: return elt
        
        self.lru[key] = (elt[0], self.age)
        return elt[0]
        

    def put(self, key: 'int', value: 'int') -> 'None':
        
        self.age += 1
        
        if self.cap == 0: return
        
        # easy case (updating an existing elt or below capacity)
        if len(self.lru) < self.cap or key in self.lru:
            self.lru[key] = (value, self.age)
            return
        
        #tricky case (new elt, at capacity)
        else:
            # first find the least-recently-used elt
            lowKey = None
            lowAge = math.inf
            for k in self.lru:
                tempAge = self.lru[k][1]
                if tempAge < lowAge:
                    lowAge = tempAge
                    lowKey = k
            
            # remove it and insert the new key-value pair (with an updated age-bit)
            self.lru.pop(lowKey)
            self.lru[key] = (value, self.age)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class KthLargest:
# this problem was really bad
# why does the add method also return the kth largest elt in the stream
# why isn't there just like a method to return that
# why is there no documentation for any of this
# like, no explanation for what we're actually supposed to do
# it never even actually says what the add method is supposed to do
# like, it literally never says the part where you're supposed to add it to the list
# it just says return the kth-largest element
# which, i mean, okay, sometimes you can just figure it out from context
# but in a problem on a site designed to help teach people how to answer coding questions
# so they can get jobs
# with companies that probably don't want them writing weird undocumented code
# with terrible method names and like overall design
# you probably don't want very many problems like this.
# i mean half of people get this problem wrong
# but the answer, obviously, is trivial
# (once you figure out a reasonably efficient built-in pythonic way to insert new elements into a list
# instead of doing it by hand like an animal).
# so maybe the really really bad question design is, like, by design
# because the problem itself is trivial
# and they needed to do something to make 27,000 of the 47,000 submissions be wrong.

    def __init__(self, k: 'int', nums: 'List[int]'):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: 'int') -> 'int':
        bisect.insort(self.nums, val)
        return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# uh huh super helpful guys thanks

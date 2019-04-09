class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0 #tricky tricky
        ls = s.split()
        if not ls: return 0 # i too like spicing up stupidly trivial problems w/ inane inputs
        return len(ls[-1])

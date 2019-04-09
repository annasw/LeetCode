"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # first a recursive solution
        if not root: return []
        if not root.children: return [root.val]
        
        ls = []
        for i in root.children:
            ls = ls + self.postorder(i)
        ls = ls + [root.val]
        return ls
        
        # and now an iterative solution
        # although for the record iteration and trees go together... poorly.
        
        # tbh right now i'm too tired to finish this but there's a decent chance i'll finish it tomorrow
        # honestly i'm exhausted, i already solved the problem the intuitive way,
        # and i'm gonna store it on github before i go to bed so i don't lose it
        # but for the record it's just an iterative dfs (which is a shitty way to code a dfs)
        # and we just shove stuff in a stack. idk i'm so tired you guys.
        
        '''if not root: return []
        if not root.children: return [root.val]
        
        ls = [] # an actual list of the elts
        stack = [] # the stack we're drawing from'''

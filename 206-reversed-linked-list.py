# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if head == None or head.next == None: return head
        
        # the code
        # works but space-bad
        # creates a new linked list instead of changing the original in place
        # but not because i'm bad at programming
        # even though i am
        i = head
        j = head.next
        
        a = ListNode(i.val)
        b = ListNode(j.val)
        a.next = None
        
        while j.next != None:
            k = j.next
            
            c = ListNode(k.val)
            b.next = a
            a = b
            b = c
            
            j = k
            i = j
            
        b.next = a
        return b
        
        
        # okay so here's the story
        # my first try was this thing
        # which i'm pretty sure works
        # but kept giving me timeouts
        # so naturally i started worrying i'd screwed something up horribly
        
        '''if head.next == None: return head
        
        i = head
        j = head.next
        
        # probably in here
        while j.next != None:
            k = j.next
            j.next = i
            i = j
            j = k
            
        j.next = head
        return j'''
        
        # but now i don't think so.
        # i think it's just
        # because see i'm a good programmer w good habits
        # so i tried to debug it
        
        # with this
        
        '''if head.next == None: return head
        
        i = head
        
        # okay so these next two work if EITHER line is in there but not with BOTH
        # why?
        # i don't know ask leetcode
        j = head.next
        #j.next = head
        '''
        
        # ughhh i wanted to reverse it in place iteratively and then recursively
        # but now i don't even have the heart to do the recursive one
        # because leetcode broke my spirit
        
        # and i don't even know if my code worked
        
        # but i'm pretty sure it did
        

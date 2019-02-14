# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        # runs in O(n) time but O(n) space
        # could stand to be a little more efficient but it's nice and straighforward anyway
        
        nll = [] # non-linked list
        p = head
        while p!=None:
            nll.append(p.val)
            p = p.next
        for i in range(len(nll)):
            if nll[i] != nll[-(i+1)]: # python is hilarious
                return False
        return True

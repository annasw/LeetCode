# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # handle edge cases
        if l1==None and l2==None:
            return [] # not sure in what way an empty list represents a nonexistent linkedlist, but...
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val<l2.val:
            newListHead = ListNode(l1.val)
            l1 = l1.next
        else:
            newListHead = ListNode(l2.val)
            l2 = l2.next
        
        newListCurrent = newListHead # pointer to current location in new list
        
        while l1 != None and l2 != None: # both lists are still alive
            if l1.val < l2.val:
                newListCurrent.next = ListNode(l1.val)
                l1 = l1.next
            else:
                newListCurrent.next = ListNode(l2.val)
                l2 = l2.next
            newListCurrent = newListCurrent.next
        
        # once one of them is none, fill out the new linkedlist with all the remaining elts in the other
        if l1 == None:
            while l2 != None:
                newListCurrent.next = ListNode(l2.val)
                newListCurrent = newListCurrent.next
                l2 = l2.next
        elif l2==None:
            while l1 != None:
                newListCurrent.next = ListNode(l1.val)
                newListCurrent = newListCurrent.next
                l1 = l1.next
        
        return newListHead

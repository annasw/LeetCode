# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listArray = [head]
        while head.next != None:
            head = head.next
            listArray.append(head)
        
        idxToRemove = len(listArray)-n
        
        if idxToRemove==0:
            if len(listArray)==1: # the resultant list will be empty... not sure what to return here. thx leetcode
                return None
            else:
                return listArray[1]
        if idxToRemove==len(listArray)-1: # last elt in listArray
            listArray[-2].next = None
            return listArray[0]
        else:
            listArray[idxToRemove-1].next = listArray[idxToRemove+1]
            return listArray[0]

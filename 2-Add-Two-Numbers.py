# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# solved the straightforward way (new linkedlist), not the tricky space-conserving way (adding backwards)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first, second = 0,0
        if l1.next==None:
            first = l1.val
        else:
            tempFirst = str(l1.val)
            while l1.next != None:
                l1 = l1.next
                tempFirst = tempFirst + str(l1.val)
            first = int(tempFirst[::-1])
        if l2.next==None:
            second = l2.val
        else:
            tempSecond = str(l2.val)
            while l2.next != None:
                l2 = l2.next
                tempSecond = tempSecond + str(l2.val)
            second = int(tempSecond[::-1])
        result = first+second
        res = str(result)[::-1]
        
        head = ListNode(int(res[0]))
        headFinal = head
        res = res[1:]
        while len(res)>0:
            nextNode = ListNode(int(res[0]))
            head.next = nextNode
            head = nextNode
            res = res[1:]
        return headFinal

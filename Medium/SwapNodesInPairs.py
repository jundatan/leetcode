# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        befCurr = ListNode(0)
        befCurr.next = curr
        if curr == None:
            return head
        currNext = head.next
        if currNext != None:
            start = befCurr.next.next
        else:
            start = befCurr.next
        while currNext != None:
            afterCurr = currNext.next
            befCurr.next = currNext
            currNext.next = curr
            curr.next = afterCurr
            befCurr = curr
            curr = curr.next
            if curr == None:
                break
            currNext = curr.next
        return start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = ListNode(0)
        first.next = head
        second = head
        res = first
        while second != None:
            second.val = second.val * 2
            plusOne = second.val / 10
            second.val = second.val % 10
            if plusOne:
                first.val = first.val + plusOne
            first = first.next
            second = second.next
        if res.val == 0:
            return res.next
        return res
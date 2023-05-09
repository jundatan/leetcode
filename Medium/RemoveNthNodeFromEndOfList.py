# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        curr = head
        while curr != None:
            nodes.append(curr.val)
            curr = curr.next
        nodes.pop(len(nodes) - n)
        if len(nodes) == 0:
            return None
        res = ListNode(nodes[0])
        xd = res
        for i in range(1, len(nodes)):
            res.next = ListNode(nodes[i])
            res = res.next
        return xd
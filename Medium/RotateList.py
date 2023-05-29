# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        new_head = head
        count_head = head
        count = 0
        while count_head != None:
            count_head = count_head.next
            count += 1
        if k >= count:
            k = k % count
        for x in range(k):
            fast = fast.next
        while fast.next != None:
                fast = fast.next
                slow = slow.next
        fast.next = new_head
        new_head = slow.next
        slow.next = None
        return new_head
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        front = []
        back = []
        curr_head = head
        while curr_head != None:
            if curr_head.val < x:
                front.append(curr_head.val)
            else:
                back.append(curr_head.val)
            curr_head = curr_head.next
        start = None
        follow = None
        print(front)
        print(back)
        for y in front:
            if start == None:
                start = ListNode(y)
                follow = start
            else:
                follow.next = ListNode(y)
                follow = follow.next
        for y in back:
            if start == None:
                start = ListNode(y)
                follow = start
            else:
                follow.next = ListNode(y)
                follow = follow.next

        return start
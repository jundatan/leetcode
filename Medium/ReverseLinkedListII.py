# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        start = head
        reverse = []
        res = []
        reverse_tf = False
        count = 1
        while start != None:
            prev = ListNode(start.val)
            if count == left and count == right:
                res.append(prev)
            elif count == left:
                reverse_tf = True
                reverse.append(prev)
            elif count == right:
                reverse_tf = False
                reverse.append(prev)
                reverse = reverse[::-1]
                res.extend(reverse)
            elif reverse_tf:
                reverse.append(prev)
            else:
                res.append(prev)
            start = start.next
            count += 1
        final_res = res[0]
        final_start = final_res
        for x in range(1, len(res)):
            final_res.next = res[x]
            final_res = final_res.next
        return final_start
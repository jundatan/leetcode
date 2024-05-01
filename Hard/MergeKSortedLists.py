# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeRecursive(self, lists, res, resCurr):
        if not lists:
            return res
        smallest = None
        smallestListIndex = 0
        i = 0
        for curr in lists:
            if curr == None:
                i += 1
                continue
            currListVal = curr.val
            if smallest == None:
                smallest = currListVal
                smallestListIndex = i
            else:
                if currListVal < smallest:
                    smallest = currListVal
                    smallestListIndex = i
            i += 1
        if smallest == None:
            return res
        lists[smallestListIndex] = lists[smallestListIndex].next
        if lists[smallestListIndex] == None:
            lists.pop(smallestListIndex)
        if res == None:
            res = ListNode(smallest, None)
            resCurr = res
        else:
            resCurr.next = ListNode(smallest, None)
            resCurr = resCurr.next
        return self.mergeRecursive(lists, res, resCurr)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.mergeRecursive(lists, None, None)
    
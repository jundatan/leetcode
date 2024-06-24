class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        res = []
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        for key,value in dictionary.items():
            if value == 1:
                res.append(key)
        return res
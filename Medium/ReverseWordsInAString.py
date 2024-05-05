class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split()
        temp = temp[::-1]
        res = ""
        for i in temp:
            res += i + " "
        return res[:len(res)-1]
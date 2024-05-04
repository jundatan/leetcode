class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = False
        for i in s:
            if b and i == 'a':
                return False
            if not b and i == 'b':
                b = True
        return True
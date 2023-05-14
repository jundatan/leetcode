#Ref from: https://leetcode.com/problems/generate-parentheses/solutions/3512769/c-java-python-javascript-using-recursion-with-explanation/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.recursiveParanthesis(0, 0, res, "", n)
        return res

    def recursiveParanthesis(self, op, cl, res, cur, n):
        if 2 * n == len(cur):
            res.append(cur)
        if op < n:
            self.recursiveParanthesis(op + 1, cl, res, cur + "(", n)
        if cl < op:
            self.recursiveParanthesis(op, cl + 1, res, cur + ")", n)
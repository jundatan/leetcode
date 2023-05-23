# Ref from: https://leetcode.com/problems/count-and-say/solutions/2716455/python-made-easy-2-ways-with-without-recursion/
# Might add own solution. Found out the way.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        temp = n
        n_str = str(n)
        if str(n_str) == '1':
            return '1'
        res = self.countAndSay(temp - 1)
        final_res = []
        i = 0
        while i < len(res):
            count = 0
            x = res[i]
            while i < len(res) and x == res[i]:
                i += 1
                count += 1
            final_res.append(str(count))
            final_res.append(x)    
        return ''.join(final_res)
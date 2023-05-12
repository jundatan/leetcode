#Ref from: https://leetcode.com/problems/integer-to-roman/solutions/2962674/easiest-o-1-faang-method-ever/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hun = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tho= ["","M","MM","MMM"]
        return tho[num/1000] + hun[(num%1000)/100] + tens[(num%100)/10] + ones[(num%10)]
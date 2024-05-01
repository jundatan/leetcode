class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        try:
            index = word.index(ch)
        except:
            return word
        
        temp = word[:index + 1]
        temp = temp[::-1]
        return temp + word[index + 1:]
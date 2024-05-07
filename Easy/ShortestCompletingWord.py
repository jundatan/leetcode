class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        ls1 = []
        for i in licensePlate:
            if i.isalpha():
                ls1.append(i.lower())
        words = sorted(words, key=lambda x : len(x))
        for i in words:
            temp = i
            for j in ls1:
                print(j)
                if j in temp:
                    idx = temp.find(j)
                    temp = temp[:idx] + temp[idx+1:]
                else:
                    break
            if len(i) - len(temp) == len(ls1):
                return i
        return
class Solution(object):
    def letterCombinations(self, digits):
        output = []
        if not digits:
            return []
        numberMap = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.recursion(digits, "", numberMap, 0, output)
        return output

    def recursion(self, digits, combination, numberMap, index, output):
        if index == len(digits):
            output.append(combination)
        else:
            letters = numberMap[int(digits[index])]
            for letter in letters:
                self.recursion(digits, combination + letter, numberMap, index + 1, output)
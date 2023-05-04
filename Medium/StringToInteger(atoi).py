class Solution(object):
    def myAtoi(self, s):
        finalNo = []
        finall = 0
        pow = 0
        isNegative = False
        isNumber = False
        isCollisionPositive = False
        for c in s:
            if c == '+':
                if isNumber or isCollisionPositive or isNegative:
                    break
                isCollisionPositive = True
                continue
            if c == ' ':
                if isCollisionPositive or isNegative:
                    break
                if isNumber:
                    break
                continue
            if c == '-':
                if isNumber or isCollisionPositive or isNegative:
                    break
                isNegative = True
                continue
            if c.isnumeric():
                isNumber = True
                finalNo.append(c)
                pow = pow + 1
            if not c.isnumeric():
                break
            if isCollisionPositive and isNegative:
                finalNo = []
                break
        pow = pow - 1
        print(finalNo)
        if len(finalNo) == 0:
            return 0
        for x in finalNo:
            finall = finall + int(x) * 10 ** pow
            pow = pow - 1
        if isNegative:
            finall = finall * -1
        if finall < -2**31:
            return -2**31
        if finall > 2 ** 31 - 1 :
            return 2 ** 31 - 1
        return finall
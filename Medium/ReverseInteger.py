class Solution(object):
    def reverse(self, x):
        number = x
        order = []
        pow = 0
        isNegative = False
        if number < 0:
            isNegative = True
            number = number * -1
        
        while not number == 0:
            order.append(number % 10)
            number = number / 10
            pow = pow + 1
        
        new = 0
        pow = pow - 1
        for y in order:
            new += y * 10 ** pow
            pow = pow - 1
        if isNegative:
            new = new * -1
        if new < -2 ** 31 or new > 2 ** 31 - 1:
            return 0
        return new
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        total = 0
        x_count = 10 ** (len(num1) - 1)
        order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for x in num1:
            y_count = 10 ** (len(num2) - 1)
            for y in num2:
                x_number = order.index(x)
                y_number = order.index(y)
                total += x_number * x_count * y_number * y_count
                y_count = y_count / 10
            x_count = x_count / 10
        return str(total)
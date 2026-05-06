class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        result = 0
        num = abs(x)

        while num != 0:
            digit = num % 10
            num //= 10
            result = result * 10 + digit

        result *= sign
        if result < -(2 ** 31) or result > 2 ** 31 - 1:
            return 0
        return result
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        # handling overflowing cases
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # decide the sign of quotient
        sign = (dividend < 0) != (divisor < 0)

        # take the positive values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        # perform bitwise shifts to handle large numbers and within time limit
        while dividend >= divisor:
            tmp, multiple = divisor, 1
            while dividend >= (tmp<<1):
                tmp = tmp<<1
                multiple = multiple<<1
            dividend -= tmp
            quotient += multiple

        return -quotient if sign else quotient

# beats 87.92% runtime and 98.16% memory
# O(logN) time complexity O(1) memory
# https://leetcode.com/problems/divide-two-integers/submissions/1327298449/

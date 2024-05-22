class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dividend_negative = (dividend < 0)
        divisor_negative = (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = dividend / divisor
        
        if dividend_negative:
            quotient *= -1
        if divisor_negative:
            quotient *= -1
            
        if quotient == 2**31:
            quotient -= 1
            
        return quotient
            
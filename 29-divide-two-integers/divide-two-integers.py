class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2**31 and divisor == -1 : # to maintain the quotient within the int range for 32 bit signed int

            return 2**31 - 1
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1 

        abs_dividend, abs_divisor = abs(dividend), abs(divisor)

        quotient = 0

        while abs_dividend >= abs_divisor:

            cnt = 0

            while (abs_divisor << (cnt + 1)) <= abs_dividend :

                cnt += 1
            
            abs_dividend = abs_dividend - (abs_divisor << cnt)

            quotient += (1 << cnt)
        
        return quotient * sign


            

            





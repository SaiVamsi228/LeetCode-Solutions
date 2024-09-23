class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)

        carry = 1

        for i in reversed(range(n)):

            if carry == 0:

                break

            if 0 <= digits[i] <= 8:

                digits[i] += 1

                carry = 0
            
            elif digits[i] == 9 :

                digits[i] = 0

                carry = 1
        
        if carry:

            digits = [1] + digits
        
        return digits




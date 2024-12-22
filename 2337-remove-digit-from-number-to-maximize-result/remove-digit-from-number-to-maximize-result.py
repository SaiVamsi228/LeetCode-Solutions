class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        ans = ""

        for i in range(len(number)):
            
            if number[i] == digit:

                newNumber = number[:i] + number[i+1:]

                if newNumber > ans :

                    ans = newNumber

        return "".join(ans)
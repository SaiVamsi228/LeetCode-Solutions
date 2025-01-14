class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        mx = -1

        n = len(num)

        for i in reversed(range(n)):

            integer = int(num[i])

            if integer % 2 == 1:

                index = i

                return num[:index+1]
        
        return ""
                
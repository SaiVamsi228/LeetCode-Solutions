class Solution:
    def countAndSay(self, n: int) -> str:
        
        cAS = "1"

        for i in range(1,n):

            res = ""

            char , freq = cAS[0], 1

            for j in range(1,len(cAS)):

                if cAS[j] != char:

                    res += str(freq)

                    res += char

                    char = cAS[j]

                    freq = 1
                
                else:

                    freq += 1
            
            if freq :

                res += str(freq)

                res += char
            
            cAS = res

        return cAS


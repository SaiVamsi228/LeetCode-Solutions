class Solution:
    def compressedString(self, word: str) -> str:
        
        newString = []

        prevChar = word[0]

        cnt = 0

        for char in word:

            if cnt == 9 or char != prevChar:

                newString.append(str(cnt) + prevChar)

                prevChar = char 

                cnt = 1

            elif char == prevChar :

                cnt += 1
    
            
        
        newString.append(str(cnt) + prevChar)

        ans = "".join(newString)

        return ans
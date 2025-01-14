class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = []

        curWord = []

        for char in s:

            if char == " ":
                
                if curWord :

                    words.append("".join(curWord))
                
                    curWord = []
            
                else:

                    pass
            
            else:

                curWord.append(char)
        
        if curWord :

            words.append("".join(curWord))

            curWord = []

        n = len(words)

        for i in range(n//2):

            words[i], words[n-i-1] = words[n-i-1] , words[i]

        res = " ".join(words)

        return res

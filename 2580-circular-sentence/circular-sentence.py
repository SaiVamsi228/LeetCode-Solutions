class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        words = sentence.split()

        prevEnding = words[-1][-1]

        for word in words:

            if word[0] != prevEnding :

                return False
            
            prevEnding = word[-1]
        
        return True
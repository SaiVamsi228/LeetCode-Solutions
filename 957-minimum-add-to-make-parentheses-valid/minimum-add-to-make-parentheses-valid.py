class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        o = 0

        c = 0

        moves = 0

        for char in s:

            if char == "(":

                o += 1
            
            else:

                if o :

                    o -= 1
                
                else:

                    moves += 1
        
        if o :

            moves += o
        
        return moves
            
        
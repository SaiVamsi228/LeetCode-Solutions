class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def getAllParen(opened,closed,arr):

            if closed > opened:

                return 

            if opened == n and closed == n:

                my_p = "".join(arr)

                ans.append(my_p)

                return

            if opened + 1 <= n :

                arr.append("(")
                
                getAllParen(opened+1,closed,arr)

                arr.pop()
            
            if closed + 1 <= n :
                
                arr.append(")")

                getAllParen(opened, closed + 1 , arr)

                arr.pop()
        
        arr = []

        opened = closed = 0

        getAllParen(opened, closed, arr)

        return ans
            



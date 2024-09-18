class Solution:

    




    
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = []

        def genLetterCasePerm(IP, OP):

            if IP == "":

                ans.append(OP)

                return
            
            OP1 = OP

            OP2 = OP

            if IP[0].isnumeric() :

                OP1 = OP1 + IP[0]

                IP = IP[1:]

                genLetterCasePerm(IP, OP1)
                
            
            else:

                OP1 = OP1 + IP[0].swapcase()
                
                OP2 = OP2 + IP[0]

                IP = IP[1:]

                genLetterCasePerm(IP, OP1)
            
                genLetterCasePerm(IP, OP2)
        
        genLetterCasePerm(s, "")

        return ans
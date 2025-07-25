class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        

        def genExpr(ind,target,expr):

            if ind >= n:

                exp = "".join(expr)
                
                # check

                if eval(exp) == target:

                    ans.append(exp)
                
                return 
            
            bin_opr_arr = ["+","-","*"]

            if num[ind] == "0":

                i = ind

                while i<n and num[i] == 0:

                    i += 1

                right = i + 1

            else:

                right = n
                
            for end in range(ind,right):

                expr.append(num[ind:end+1])

                if end != n-1:

                    for opr in bin_opr_arr:

                        # save

                        expr.append(opr)

                        # recurse

                        genExpr(end+1,target,expr)

                        # backtrack

                        expr.pop()
                    
                else:

                    genExpr(end+1,target,expr)
                
                expr.pop()

        ans = []

        n = len(num)

        genExpr(0,target,[])

        return ans







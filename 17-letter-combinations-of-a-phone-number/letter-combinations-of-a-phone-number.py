class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hm = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        combs = []

        def getAllCombs(ind,comb):

            if ind == n:

                combs.append("".join(comb))

                return
            
            cur_poss = hm[int(digits[ind])]

            no_of_chars = len(cur_poss)

            for i in range(no_of_chars):

                comb.append(cur_poss[i])

                getAllCombs(ind+1,comb)

                comb.pop()
            
        n = len(digits)

        if digits == "":

            return []

        getAllCombs(0,[])

        return combs

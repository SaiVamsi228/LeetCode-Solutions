class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0 for j in range(i+1)] for i in range(numRows)]

        for i in range(numRows):

            row = ans[i]

            for j in range(i+1):

                if j == 0 or j == i :

                    row[j] = 1

                    continue
                
                row[j] = ans[i-1][j] + ans[i-1][j-1]
        
        return ans







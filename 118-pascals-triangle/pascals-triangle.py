class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        res = []

        for length in range(1,numRows+1):

            arr = [0 for i in range(length)]

            arr[0] = arr[-1] = 1

            for j in range(length):

                if j == 0 or j == length - 1 :

                    continue
                
                arr[j] = res[-1][j] + res[-1][j-1]
            
            res.append(arr)
            
        return res
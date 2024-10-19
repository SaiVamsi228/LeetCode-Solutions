class Solution:
    def invert(self, arr):

        newArr= []

        for char in arr:

            if char == "0":

                newArr.append("1")
            
            else:

                newArr.append("0")

        return newArr
    
    def reverse(self, arr):

        return arr[::-1]

    def getBinStr(self, n, arr):

        if n == 1:

            return ["0"]
        
        prevHalf = self.getBinStr(n-1, arr)

        nextHalf = self.reverse(self.invert(prevHalf))

        myStr = prevHalf + ["1"] + nextHalf

        return myStr

    def findKthBit(self, n: int, k: int) -> str:

        s = self.getBinStr(n, [])

        return s[k-1]
class Solution:
    def maximumSwap(self, num: int) -> int:

        arr = [int(x) for x in str(num)]

        n = len(arr)
        
        miniIndFromLeft = [0 for i in range(n)]

        maxIndFromRight = [0 for i in range(n)]


        miniInd = 0

        miniIndFromLeft[0] = 0

        for i in range(1,n):

            if arr[i] < arr[miniInd]:

                miniInd = i
            
            miniIndFromLeft[i] = miniInd
        
        maxiInd = n - 1

        maxIndFromRight[n-1] = n - 1
        
        for i in reversed(range(n-1)):

            if arr[i] > arr[maxiInd] :

                maxiInd = i
                
            maxIndFromRight[i] = maxiInd
        
        print(miniIndFromLeft)

        print(maxIndFromRight)
        for i in range(n):

            if arr[miniIndFromLeft[i]] < arr[maxIndFromRight[i]]:

                arr[miniIndFromLeft[i]], arr[maxIndFromRight[i]] = arr[maxIndFromRight[i]], arr[miniIndFromLeft[i]]
            
                break
        
        arr = [ str(x) for x in arr]

        finalAns = int("".join(arr))

        return finalAns





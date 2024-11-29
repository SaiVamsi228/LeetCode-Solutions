class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        q = [i for i in range(1,n+1)]

        while len(q) != 1:

            for i in range(k-1):

                q.append(q.pop(0))

            q.pop(0)
        
        return q[0]
            


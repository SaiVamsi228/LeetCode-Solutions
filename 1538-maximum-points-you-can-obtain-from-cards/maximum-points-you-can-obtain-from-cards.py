class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)

        totalScore = 0

        if k == n:

            return sum(cardPoints)

        i = n - k

        j = i

        curSum = mx = 0

        while True:
            
            print(i,j,curSum)
            curSum += cardPoints[j]

            if (i <= j and j - i + 1 < k) or (i>j and n-i+j+1 < k):

                j += 1

                j = j % n

            elif (i <= j and j - i + 1 == k) or (i>j and n-i+j+1 == k):

                mx = max(mx, curSum)

                curSum -= cardPoints[i]

                i += 1

                i = i % n

                if i == 1:

                    break

                j += 1 

                j = j % n
        
        return mx









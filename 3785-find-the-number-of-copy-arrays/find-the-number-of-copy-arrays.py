class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        
        low = bounds[0][0]

        high = bounds[0][1]

        n = len(original)

        for i in range(1,n):

            diff = original[i] - original[i-1]

            low = max(low + diff, bounds[i][0])

            high = min(high + diff, bounds[i][1])
        
        if high - low + 1 > 0:

            return high - low + 1
        
        return 0
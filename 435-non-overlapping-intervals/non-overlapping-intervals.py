class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        n = len(intervals)

        if n == 1:

            return 0
        
        ps, pe = intervals[0]

        overlapping = 0

        for i in range(1,n):

            cs, ce = intervals[i]

            if cs < pe:

                overlapping += 1
                # missing: update pe to the smaller end time
                if ce < pe:

                    ps, pe = cs, ce  # keep the one with smaller end

            else:
                
                ps, pe = cs, ce
        
        return overlapping
            
            

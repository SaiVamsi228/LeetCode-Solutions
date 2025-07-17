class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        merged = []

        prev_s, prev_e, cur_s, cur_e = None, None, None, None

        n = len(intervals)

        for i in range(n):
            
            interval = intervals[i]

            cur_s, cur_e = interval[0] , interval[1]

            if prev_s == None and prev_e == None:

                prev_s, prev_e = cur_s, cur_e
            
                continue
            
            if cur_s <= prev_e:

                if cur_e > prev_e:

                    prev_e = cur_e
                
                else:

                    prev_e = prev_e
            
            else:

                merged.append([prev_s,prev_e])

                prev_s , prev_e = cur_s, cur_e
        
        if prev_s != None and prev_e != None:

            merged.append([prev_s, prev_e])
        
        return merged
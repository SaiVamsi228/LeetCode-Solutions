class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)

        if n == 1:

            return intervals
        
        sorted_intervals = sorted(intervals)

        st = []

        st.append(sorted_intervals[0])

        for i in range(1,n):

            a,b  = st.pop()

            c,d = sorted_intervals[i]

            if d <= b :

                merged_interval = [a,b]

                st.append(merged_interval)


            elif c <= b :

                merged_interval = [a,d]

                st.append(merged_interval)
            
            else:

                st.append([a,b])

                st.append([c,d])
        
        return st



        
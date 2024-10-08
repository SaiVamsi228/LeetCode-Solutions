class Solution:
    def minSwaps(self, s: str) -> int:
        
        arr = [ x for x in s]

        n = len(arr)

        i, j = 0, n - 1

        swaps = 0

        o = c = 0

        while i <= j  :

            char = arr[i]

            if char == "[":

                o += 1
            
            else:

                c += 1
            
            if c > o :

                swaps += 1

                while arr[j] != "[":

                    j -= 1
                
                arr[i], arr[j] = arr[j],arr[i]

                o += 1

                c -= 1

            i += 1
        
        return swaps

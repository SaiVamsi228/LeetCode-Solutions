from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        letter_count = Counter(s)

        hp = []

        heapify(hp)

        for char,freq in letter_count.items():

            heappush(hp,(-freq,char))
        
        res = []

        print(hp)

        while hp:

            freq, char = heappop(hp)

            freq = -1 * freq

            for _ in range(freq):

                res.append(char)
        
        return "".join(res)






        
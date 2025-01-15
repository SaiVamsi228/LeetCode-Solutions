from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:

        hash_map = defaultdict(int)

        for char in s:

            hash_map[char] += 1
            
        hash_map = dict(reversed(sorted(hash_map.items(), key = lambda item: item[1])))

        ans = []

        for char, freq in hash_map.items():

            for _ in range(freq):

                ans.append(char)


        return "".join(ans)



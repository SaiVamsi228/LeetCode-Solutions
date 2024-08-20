from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashMap = dict()

        i = 0 

        j = 0

        n = len(s)

        maxFreq = mx = 0

        

        while j < n :

            if s[j] not in hashMap:
                
                hashMap[s[j]] = 1

            else:

                hashMap[s[j]] += 1

            maxFreq = max(maxFreq, hashMap[s[j]])

            if j - i + 1 - maxFreq <= k :

                mx = max(mx, j - i + 1)

                j += 1
            
            elif j - i + 1 - maxFreq > k :

                while j - i + 1 - maxFreq > k :

                    hashMap[s[i]] -= 1

                    for char, cnt in hashMap.items():

                        maxFreq = max(maxFreq, cnt)

                    i += 1

                j += 1

        return mx 
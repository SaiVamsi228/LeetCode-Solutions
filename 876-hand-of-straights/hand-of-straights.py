from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hm = Counter(hand)

        hand.sort()

        i = 0

        n = len(hand)

        if n % groupSize != 0:

            return False

        num_of_grps = n // groupSize

        for _ in range(num_of_grps):

            while i < n and hm[hand[i]] == 0:

                i += 1
            
            start = hand[i]

            for num in range(start,start + groupSize):

                if hm[num] > 0:

                    hm[num] -= 1

                    continue
                
                else:

                    return False
    
        return True
            



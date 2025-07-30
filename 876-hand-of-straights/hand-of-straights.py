from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        minHeap = list(count.keys())
        heapify(minHeap)

        while minHeap:
            first = minHeap[0]  # Smallest available card

            for i in range(groupSize):
                card = first + i
                if count[card] == 0:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    if card != minHeap[0]:
                        return False
                    heappop(minHeap)

        return True

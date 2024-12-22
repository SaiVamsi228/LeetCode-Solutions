class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hMap = {}

        mini = float('inf')

        for ind,card in enumerate(cards):

            if card not in hMap:

                hMap[card] = ind
            
            else: # card in hashMap

                length = ind - hMap[card] + 1

                mini = min(mini, length)

                hMap[card] = ind
    
        if mini == float('inf'):

            return -1
    
        return mini


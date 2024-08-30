from collections import deque
from heapq import heapify, heappush, heappop
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:

            return []

        q = deque()
        index = 0
        curLevel = 0

        hPair = (index, curLevel, root.val)

        minHeap = []

        heapify(minHeap)

        heappush(minHeap, hPair)

        qPair = (index, curLevel, root.val, root)

        q.append(qPair)

        while q:

            n = len(q)

            for i in range(n):

                ind, curLevel, curNodeVal, curNode = q.popleft()

                if curNode.left :

                    qPair = (ind - 1, curLevel + 1,  curNode.left.val , curNode.left)

                    hPair = (ind - 1, curLevel + 1,  curNode.left.val )

                    heappush(minHeap, hPair )

                    q.append(qPair)

                if curNode.right :

                    qPair = (ind + 1, curLevel + 1,  curNode.right.val , curNode.right)

                    hPair = (ind + 1, curLevel + 1,  curNode.right.val )

                    heappush(minHeap, hPair)

                    q.append(qPair)

        vOrder = []

        prevInd = 0.1

        vLevel = []

        while minHeap:

            ind, curLevel, curNodeVal= heappop(minHeap)

            if ind != prevInd and prevInd != 0.1:

                vOrder.append(vLevel)

                vLevel = []

            vLevel.append(curNodeVal)

            prevInd = ind
        
        if vLevel: # For the last Level

            vOrder.append(vLevel)
                
        return vOrder




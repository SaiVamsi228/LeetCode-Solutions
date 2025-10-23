class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        n = len(edges)
        
        score = [0 for i in range(n)]

        for u,v in enumerate(edges):

            score[v] += u
        
        mx = max(score)

        return score.index(mx)
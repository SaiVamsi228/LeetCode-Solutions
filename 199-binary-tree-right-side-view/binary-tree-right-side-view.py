# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:

            return []

        ans = []

        q = deque()

        q.append(root)

        while q:

            n = len(q)

            last_found = None

            for i in range(n):

                node = q.popleft()

                last_found = node

                if node.left:

                    q.append(node.left)
                
                if node.right:

                    q.append(node.right)
            
            ans.append(last_found.val)
        
        return ans
                

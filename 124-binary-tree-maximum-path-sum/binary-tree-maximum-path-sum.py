# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        mx = float('-inf')

        def getMaxSumOfTheBranch(node):

            nonlocal mx

            if node == None:
                
                return 0
            
            ls = getMaxSumOfTheBranch(node.left)

            rs = getMaxSumOfTheBranch(node.right)

            ls = ls if ls > 0 else 0

            rs = rs if rs > 0 else 0

            mx_sum_passing_through_node = ls + rs + node.val

            mx = max(mx,mx_sum_passing_through_node)

            return max(ls,rs) + node.val
        
        getMaxSumOfTheBranch(root)

        return mx

        
        


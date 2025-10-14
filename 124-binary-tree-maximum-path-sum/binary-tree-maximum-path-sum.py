# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mx_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def getMaxSum(root):

            if not root:

                return 0
            
            leftMaxSum = getMaxSum(root.left) 

            rightMaxSum = getMaxSum(root.right)

            leftMaxSum = leftMaxSum if leftMaxSum > 0 else 0

            rightMaxSum = rightMaxSum if rightMaxSum > 0 else 0

            self.mx_sum = max(self.mx_sum,leftMaxSum+rightMaxSum+root.val)

            return max(leftMaxSum,rightMaxSum) + root.val
        
        getMaxSum(root)

        return self.mx_sum
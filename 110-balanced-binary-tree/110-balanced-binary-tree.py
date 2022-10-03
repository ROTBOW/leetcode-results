# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root) :
            
            if not root : 
                return 0, True
            else :
                left, lstat = dfs(root.left)
                right, rstat = dfs(root.right)
                
                status = lstat and rstat and abs(left-right)<=1
                return max(left,right)+1, status
        
        
        n, status = dfs(root)
        return status
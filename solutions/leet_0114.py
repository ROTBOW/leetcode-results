TITLE = 'Flatten Binary Tree to Linked List'
'''
time: BigO()
space: BigO()

Results:
    Runtime: 76 ms, faster than 14.92%
    Memory Usage: 15.1 MB, less than 99.51%
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root == None: return None
        
        stack = [root]
        nodes = []
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)

            nodes.append(node)
            
        prev = nodes[0]
        for i in range(1, len(nodes)):
            prev.left = None
            prev.right = nodes[i]
            prev = prev.right
        
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root, root.val)]
        res = 0

        while stack:
            node, rtl = stack.pop()

            if not node.left and not node.right:
                res += int(rtl)
                continue

            if node.left:
                stack.append((node.left, f"{rtl}{node.left.val}"))

            if node.right:
                stack.append((node.right, f"{rtl}{node.right.val}"))

        return res
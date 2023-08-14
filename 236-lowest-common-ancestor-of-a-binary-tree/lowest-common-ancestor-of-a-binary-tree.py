# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(s, t, path):
            if s.val == t:
                return True
            
            if s.left and search(s.left, t, path):
                path.append(s.left)

            elif s.right and search(s.right, t, path):
                path.append(s.right)

            return path

        t1, t2 = [], []
        search(root, p.val, t1)
        search(root, q.val, t2)
        
        ans = root
        while t1 and t2 and t1[-1].val == t2[-1].val:
            ans = t1.pop()
            t2.pop()

        return ans
TITLE = 'Step-By-step directions from a binary tree node to another'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 811 ms, faster than 79.81%
    Memory Usage: 137.2 MB, less than 43.24%
'''
class Solution:
    def getDirections(self, root, startValue, destValue):

        def find(n, val, path):
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path

        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))
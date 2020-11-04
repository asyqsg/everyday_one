# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return []

        deque = [root]
        res = []

        while deque:
            cur = deque
            nextlayer = []
            for node in cur:
                res.append(node.val)
                if node.left:
                    nextlayer.append(node.left)
                if node.right:
                    nextlayer.append(node.right)
            deque = nextlayer
        return res
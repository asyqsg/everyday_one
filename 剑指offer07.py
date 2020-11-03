# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if not preorder or not inorder: return

        root_val = preorder[0]
        root = TreeNode(root_val)
        index_inorder = inorder.index(root_val)
        left_inorder = inorder[:index_inorder]
        right_inorder = inorder[index_inorder + 1:]

        size_l = len(left_inorder)
        size_r = len(right_inorder)
        left_preorder = preorder[1:1 + size_l]
        right_preorder = preorder[1 + size_l:]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

if __name__ == '__main__':
    s = Solution().buildTree([3,9,20,15,7],[9,3,15,20,7])
    print('a')
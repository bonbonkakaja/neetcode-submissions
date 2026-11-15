# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def heightOfBinaryTree(self, root: Optional[TreeNode]):

        if(root==None ):
            return 0
        lh=self.heightOfBinaryTree(root.left)
        rh=self.heightOfBinaryTree(root.right)
        ch=max(lh,rh)+1
        self.res=max(self.res,lh+rh)
        return ch
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        self.heightOfBinaryTree(root)
        return self.res
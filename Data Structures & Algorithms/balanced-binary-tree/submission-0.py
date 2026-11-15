# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self,root):
        if(not root):
            return 0
        l=self.getHeight(root.left)
        r=self.getHeight(root.right)
        return max(l,r)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not root):
            return True
        l=self.getHeight(root.left)
        r=self.getHeight(root.right)
        isb=abs(l-r)<=1
        if(not isb):
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
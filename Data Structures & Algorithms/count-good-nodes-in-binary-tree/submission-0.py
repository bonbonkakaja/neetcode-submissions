# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, max_before):
            if not node:
                return None
            if node.val >= max_before:
                self.res +=1
            max_before=max(max_before,node.val)
            dfs(node.left,max_before)
            dfs(node.right,max_before)
        dfs(root,root.val)
        return self.res

        
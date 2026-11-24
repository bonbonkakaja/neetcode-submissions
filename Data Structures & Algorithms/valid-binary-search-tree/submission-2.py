# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,upper_bound,lower_bound):
            if not node:
                return True
            
            # Top down
            rule1 = False
            rule2 = False
            if (upper_bound is not None):
                rule1 = node.val < upper_bound 
            else:
                rule1 = True
            if (lower_bound is not None):
                rule2 = node.val > lower_bound
            else:
                rule2=True
            isLeftValid=dfs(node.left, node.val, lower_bound)
            isRightValid=dfs(node.right,upper_bound,node.val)
            return rule1 and rule2 and isLeftValid and isRightValid
        return dfs(root,None,None)



            
            
        
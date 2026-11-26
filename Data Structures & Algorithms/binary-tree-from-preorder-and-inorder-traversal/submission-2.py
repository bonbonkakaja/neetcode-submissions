# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = dict()
        for i,other in enumerate(inorder):
            hashmap[other]=i
        def dfs(preorder,inorder,l,r):
            if(len(preorder)==0):
                return None
            root_val= preorder[0]
            root=TreeNode(root_val)
            index=None
            if(l is None or r is None or l>=r):
                return None
            '''
            for i in range(l,r):
                if(inorder[i]==root.val):
                    index=i
            '''
            index=hashmap[root.val]
            preorder.pop(0) # important to pop AFTER checking range so a empty range return None before it consume a preorder node
            lefttree=dfs(preorder,inorder,l,index)
            righttree=dfs(preorder,inorder,index+1,r)
            root.left=lefttree
            root.right=righttree
            return root
        return dfs(preorder,inorder,0,len(preorder))



        
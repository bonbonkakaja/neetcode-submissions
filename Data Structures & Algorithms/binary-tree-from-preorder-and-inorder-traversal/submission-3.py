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

             # important to checking range before Pop the preorder so a empty range return None before it consume a preorder node -> empty range always mean we are hitting the bottom (AI help me realize this..)
            if(l is None or r is None or l>=r):
                return None
            if(len(preorder)==0):
                return None
            root_val= preorder.pop(0)
            root=TreeNode(root_val)
            index=None
            '''
            for i in range(l,r):
                if(inorder[i]==root.val):
                    index=i
            '''
            index=hashmap[root.val]
            lefttree=dfs(preorder,inorder,l,index)
            righttree=dfs(preorder,inorder,index+1,r)
            root.left=lefttree
            root.right=righttree
            return root
        return dfs(preorder,inorder,0,len(preorder))



        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #in order traversal
        res = []
        
        #make the inorder traversal function
        def inorder(root):
            #base case
            if root==None:
                return None
            else:
                #left then root then right
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res

        
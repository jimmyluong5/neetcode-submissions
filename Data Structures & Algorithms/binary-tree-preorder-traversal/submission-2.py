# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #create empty array to return after
        res = []

        #helper function
        def preorder(root):
            #base case
            if root ==None:
                return None
            else:
                #root first
                res.append(root.val)
                #left then right
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res
        
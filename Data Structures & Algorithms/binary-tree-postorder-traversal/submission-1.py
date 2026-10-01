# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postorder(root):
            #base case
            if root == None:
                return None
            else:
                #left then right then root
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        postorder(root)
        return res
        
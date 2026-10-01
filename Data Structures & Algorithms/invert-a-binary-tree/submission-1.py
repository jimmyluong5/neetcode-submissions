# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #just swap the pointers at the children, then recurse down the left and right to do the same thing

        #base case is if the root is none
        if root == None:
            return None
        else:
            #swap the left and right children
            temp = root.left
            root.left = root.right
            root.right = temp
        
            #recurse down the left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
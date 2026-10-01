# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        self.res = True
        #if the heights aren't differing in height by no more than 1
        def dfs(curr):
            if curr == None:
                return 0
            
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            #from that we can calculate the res
            diff = abs(leftHeight-rightHeight)
            if diff > 1:
                self.res = False
            return 1+max(leftHeight, rightHeight)
        
        #we dfs down left then right then calculate the difference between the two
        dfs(root)
        return self.res

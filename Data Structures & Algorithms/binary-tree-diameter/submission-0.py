# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter of binary tree can include more than 1 node, it can be 2 nodes or more attached

        #make the global variable of the max diameter
        self.max_diameter=0
        #make the dfs function that returns the height of a node
        def dfs(curr):
            if curr == None:
                return 0
            
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)

            #calculate the diameter
            diameter = leftHeight + rightHeight

            #find the max diameter #this always updates the max diameter,
            self.max_diameter = max(self.max_diameter, diameter)

            #return the height
            return 1+max(leftHeight, rightHeight)

        #call teh dfs function to find the height of a node
        dfs(root)
        #return the max diameter, once we call the dfs function, the 
        #max diameter variable should be filled.
        return self.max_diameter

        
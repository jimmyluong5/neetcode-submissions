# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] #
        stack = [] #call stack
        curr = root #which lets curr get the attirbutes of a tree node

        #so as long as curr is not Null and the stack is not empty
        while curr or stack:
            #we just go to the left
            
            #then we check again while our current node is not null we go left and add the values
            #to the call stack if it is null
            #then we add the last value we added to the call stack to the resulting array
            while curr:
                stack.append(curr)
                curr = curr.left

            #we pop from our call stack, and add it to
            curr = stack.pop()
            res.append(curr.val)
            #then we go to the right
            curr = curr.right
        return res
        
            

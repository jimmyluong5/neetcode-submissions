# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #make two stacks
        res = []
        stack = [root] #initialize the call stack with the root already
        #curr = root
        if root == None:
            return []
        #for these problems we want to append the stuff that we don't want first
        #so if we want the traverse the left side, append all the stuff on the right on the call stack first
        #then append the left stuff and pop it to the resulting array
        #as long as the stack is not empty
        while stack:
            #whatever is on the call stack, each time we run the while loop we append it to res
            curr = stack.pop() 
            res.append(curr.val)

            #then we append the right nodes on the call stack 
            if curr.right:
                stack.append(curr.right)
            #if it is null then we just loop back to the top.
            if curr.left:
                stack.append(curr.left)
        return res


            
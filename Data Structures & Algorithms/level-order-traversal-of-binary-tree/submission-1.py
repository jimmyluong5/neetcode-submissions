# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return res
        
        #make the queue
        queue = collections.deque()
        #append the root
        queue.append(root)

        #loop thorugh the queue while its not empty
        while queue:
            #create the sublists for each level
            sublist = []
            
            #loop through each level of the tree
            for i in range(len(queue)):
                #pop the left most node and add it to the queue
                node = queue.popleft()
                #then add the nodes value to the sublist
                sublist.append(node.val)

                #then add the left and right child to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            #then we need to add up all the sublists together and put it in result list
            res.append(sublist)
        
        return res

            
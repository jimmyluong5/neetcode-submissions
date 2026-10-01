# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #create the res array
        res = []
        
        
        #we need to use a queue for using bfs, 
        #we need to create a queue
        q = collections.deque()

        #then we append the first node to the queue
        q.append(root)

        #then we keep appending while the q is not empty or not null

        while q:
            #we need to get the length of the queue and loop through every value
            qlen = len(q)
            #then we need to add those values to its own individual list
            level = []
            for i in range(qlen):
                #we need to pop nodes from the left of the queue
                node = q.popleft()
                #also check if the node is null
                if node is not None:
                    level.append(node.val) #add the node to the sublist
                    #then add the children to the queue
                    q.append(node.left) #starting from the left
                    q.append(node.right) #right child next
            #then after we have finished with every single level, we need to combine all the sublists into the result list
            
            #if our the level is not empty because we don't want to add empty levels.
            if level:    
                res.append(level)
        #keep running the outer loop until there are no more nodes in the queue

        return res
            
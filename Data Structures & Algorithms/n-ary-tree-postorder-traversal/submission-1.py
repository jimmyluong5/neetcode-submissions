"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #just go visit the children first, then the root.
        res = []
        
        def dfs(node):
            if node == None:
                return 0

            #go through every child
            for child in node.children:
                #we call dfs
                dfs(child)
            #append the current nodes value to the result.
            res.append(node.val)
        dfs(root)
        return res

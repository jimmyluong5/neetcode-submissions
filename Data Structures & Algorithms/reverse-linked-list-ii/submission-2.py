# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #create dummy node
        dummy = ListNode(-1, head)
        curr = dummy.next
        leftprev = dummy #we need to place leftprev before the left node 
        #and to do that its left-1
        for i in range(left-1):
            leftprev = curr
            curr=curr.next
        #now that leftprev is at the location before left

        #we just need to reverse from right-left+1
        #we can just do this with iterations
        prev = None

        for i in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        #then we need to connect the left node with the last node, and we can access that
        #using leftprev.next.next #which curr is either on the last node or pointing to null which is fine.
        leftprev.next.next = curr 
        leftprev.next = prev
        return dummy.next
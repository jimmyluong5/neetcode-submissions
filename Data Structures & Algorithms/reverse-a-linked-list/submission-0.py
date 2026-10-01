# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first we want to assign some ptrs
        prev = None
        curr = head

        while curr != None:
            #create another pointer that allows curr to move forward
            next = curr.next #or head.next.next

            #then we move the head's ptr backwards, move all the ptrs forwards by one starting with prev, then curr, then next
            curr.next = prev
            
            prev = curr
            curr = next
        return prev #return this because curr will hit None then prev with be the new head.
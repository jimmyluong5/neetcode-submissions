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
        leftprev = dummy

        #we need to iterate through the linked list until we place curr at left and prev at left-1
        for i in range(left-1):
            leftprev = curr
            curr = curr.next

        #after that we can just simply reverse the linked list starting from left to right-1eft+1   
        prev = None
        #here curr is at left already
        for i in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        #now that we reverse the linked list
        #we still have access to the first node via 
        #dummy.next.next, we can do leftprev.next, but 
        leftprev.next.next = curr
        leftprev.next = prev
        return dummy.next


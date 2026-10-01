# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #set two pointers then a third in the loop
        curr = head
        prev = None

        while curr != None:
            next = curr.next

            #then then curr.next = prev
            curr.next = prev

            #move prev
            prev = curr
            #move curr
            curr = next
        return prev

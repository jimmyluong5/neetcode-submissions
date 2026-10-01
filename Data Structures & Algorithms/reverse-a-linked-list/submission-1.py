# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #set up two pointers, prev for behind the head node, curr on the head node
        prev = None
        curr = head

        while curr!= None:
            #make another ptr which is next, which will always move each iteration
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
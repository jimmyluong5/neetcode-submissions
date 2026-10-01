# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node and 2 ptrs
        p1 = head1
        p2 = head2

        #dummy node with a value of -1, doesn't matter the value, in the end we will return dummy.next
        #for the head of the linked list we're going to build
        dummy = ListNode(-1)

        #create curr which will help us link the elements together
        curr = dummy

        #now while p1 and p2 is not null
        while p1 and p2!=None:
            #then we check if p1.val < p2.val, if not then curr.next = p2
            if p1.val < p2.val:
                curr.next = p1
                #we move p1
                p1 = p1.next
                #move curr
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        #we break the loop if one of our ptrs hits null

        #in case p1 hits null or if its negative, curr.next will be right behind it
        if p1 == None:
            curr.next = p2
            return dummy.next
        
        if p2 == None:
            curr.next = p1
            return dummy.next
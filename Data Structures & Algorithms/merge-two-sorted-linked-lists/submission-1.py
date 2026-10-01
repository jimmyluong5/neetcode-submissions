# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head1
        p2 = head2
    #need to create dummy node for the new linked list
        dummy = ListNode(-1)
        #this ptr will help us create the linked list
        curr = dummy #which points to the smaller element between p1 and p2

        while p1 !=None and p2 !=None:
            if p1.val > p2.val:
                curr.next = p2
                p2 = p2.next
                #curr = curr.next, factor out
            else:#p1.val < p2.val so we make curr point to the smaller number
                curr.next = p1
                p1 = p1.next
                #curr = curr.next #move ptr you can factor this out because its in two places.
        #if both none return dummy.next
        #its not getting that list element, because p1 gets None first
            curr = curr.next
        #we know that curr.next is right behind it based on the math
        if p1 == None:
            curr.next = p2
            return dummy.next

        elif p2 == None:
            curr.next = p1
            return dummy.next


    
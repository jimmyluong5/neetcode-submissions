# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    #helper function to reverse linked list for the 2nd half
    def reverseLL(self, head):
        curr = head
        prev = None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev



    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #we need to cut the linked list into two then we need to reverse the 2nd half
        #we need to find the middle of the linked list using fast and slow pointers
        fast = head
        slow = head #for the odd case
        prev = None #we need this pointer for the even case.

        while fast and fast.next:
            fast = fast.next.next
            prev = slow 
            slow = slow.next
        
        #after this fast is either null or on the last node.
        #last node this means that its odd

        if fast != None:
            #then we need to assign a temp pointer to that position in the middle
            #then cut it off after
            temp = slow.next
            slow.next = None
            p2 = self.reverseLL(temp)
        if fast == None:
            #this is the even case
            temp = prev.next
            prev.next = None
            p2 = self.reverseLL(temp)

        #then we can merge the linked lists alternatively
        p1 = head #this is at the head
        curr = head

        while p1 and p2:
            p1 = p1.next
            curr.next = p2

            curr = curr.next
            p2=p2.next

            curr.next = p1
            curr = curr.next
        


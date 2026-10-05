# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #check if head is null
        if head == None:
            return head

        dummy = ListNode(-1, head)
        fast = head

        #we need to determine the length of the linked list in order to know
        #how deep to go into the linked list
        tail = head
        #since we start at tail.next, our length starts at 1
        length = 1

        while tail.next:
            tail=tail.next
            length+=1

        #calculate new k 
        k = k % length

        #then we have tail on the very last node
        
        #then we need to place fast on the k-1 spot
        if k == 0:
            return head
    

        for i in range(length-k-1):
            fast=fast.next
        

        #we need to attach the tail node to the head
        tail.next = head
        #then we need to attach dummy.next to the head of the new linekd list
        dummy.next = fast.next

        #then cut off fast.next
        fast.next = None


        return dummy.next


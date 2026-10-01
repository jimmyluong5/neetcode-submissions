# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node
        dummy = ListNode(-1)

        #set a ptr for connecting the elements in the lists
        curr = dummy

        p1 = list1
        p2 = list2


        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1=p1.next
            else:
                curr.next = p2
                p2=p2.next
            curr=curr.next
        
        #then if the p1 or p2 hits none, curr will be behind one of them so we can just attach the other linked list to this list
        if p1 == None:
            curr.next = p2
            return dummy.next
        if p2 == None:
            curr.next = p1
            return dummy.next
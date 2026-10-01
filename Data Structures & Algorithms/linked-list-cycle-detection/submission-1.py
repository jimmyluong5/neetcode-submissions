# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use the fast and slow algo for cycle detection
        slow = head 
        fast = head
        while fast and fast.next != None:
            #move these ptrs
            slow = slow.next #move one forward
            fast = fast.next.next #move two forwards

            #if the memory addresses are the same, they are on the same node,
            #and if they eventually end up on the same node theres a cycle
            if slow == fast:
                return True
        return False
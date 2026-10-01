# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #dummy node
        dummy = ListNode(-1, head)
        c = dummy
        cn = c.next
        while c and cn:
            if cn.val == val:
                cn = cn.next
                c.next = cn
            
            else:
                #we move both
                #move the cn first
                cn = cn.next
                c = c.next
        return dummy.next
        
        

        
            

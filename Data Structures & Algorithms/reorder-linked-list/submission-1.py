# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reverseLL(self, p1):
        curr = p1
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head
        slow = head
        #in order for us to have two clean linked lists to merge, we need to
        #break the link between the two linked lists or else we will have an infinite loop

        #so we need an additional pointer, and it will always be 1 node behind slow so when 
        #slow is the middle pointer, prev is the node before and can point into NULL breaking the link between the 1,2,3 linked list and the 6,5,4 linked list
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if fast == None: #the list is even
            temp = prev.next #set a pointer to the head of the 2nd LL
            prev.next = None #then cut it off
            #and we use the reverseLL helper function
            p2 = self.reverseLL(temp)
        else: 
            temp = slow.next
            slow.next = None
            p2 = self.reverseLL(temp)

    
        #but odd case 
        #prev will be at 2 instead of 3 at 1,2,3,4,5, so what do we do?

        #i need to distinguish when the length is even or odd.
        #if its odd, then prev will be exactly in the middle
        #if its even then slow or prev is in the middle

        #i want the first half to be larger because if its larger than 
        #1 2 3 4 5
        #slow will be at 3

        #then the final sequence of numbers will be 
        #5 1 4 2 3 #where 2-3 is just already attached to teh first half of the linked list
        #fast.next will terminate and slow will be the middle pointer 
        #fast will be on the last node
        
        #create helper function that reverses the linked list starting from p1 which is the 
        #start of the linked list

  
       
        
        #returns the pointer to the reverse linked list

        #we can set fast equal to this since it'll be in the same position
        
        
        
        #cuz slow is the middle pointer now, and we need to reverse from the middle pointer to above.

        #then we can we technically have two linked lists and just merge based on value

        #p2 is the head of the reversed linked list

        p1 = head
        curr = head
        while p1 and p2:
            p1 = p1.next
            curr.next = p2
            p2=p2.next
            curr=curr.next
            curr.next = p1
            curr=curr.next

          

            
            

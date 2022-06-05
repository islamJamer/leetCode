# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        
        curr = head
        values = {}
        
        while curr is not None:
            if values.get(curr.val) is None:
                values[curr.val] = 1
            else: 
                values[curr.val]+=1
            curr = curr.next
                   
        if(values[head.val] > 1):
            if len(values) == 1: return None 

        first =  ListNode(0) 
        first.next = head
        head = first
        
        curr = head          
        while curr is not None:
            nextNode = curr.next
            
            while nextNode is not None and values[nextNode.val] > 1:
                nextNode = nextNode.next
            
            if nextNode is None:
                curr.next = None
            else:
                curr.next = nextNode

            curr = curr.next
        
        return head.next
        
        
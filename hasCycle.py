# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        if head.next is None: return False
        curr = head.next
        prev = head
        
        while curr is not None and prev is not None:
            if prev == curr:
                return True
            
            prev = prev.next 
            
            if curr.next:
                curr = curr.next.next
            else:
                return False
        
        
        return False
        
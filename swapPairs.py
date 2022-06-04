# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        if head.next is None: return head
        if head.next.next is None:
            temp = head.next
            head.next = None
            temp.next = head
            
            return temp 
        
        prev = head
        cur = head.next
        root = cur
        left = prev
        
        while prev is not None:
            left = prev
            temp = cur.next
            
            cur.next = prev
            prev.next = temp

            prev = temp
            
            if prev is None or prev.next is None:
                break
            cur = prev.next
            left.next = cur
            
        return root
            
            
            
        
        
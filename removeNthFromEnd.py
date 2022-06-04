# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: return []
        
        count = 0
        curr = head
        while curr is not None:
            count+=1
            curr = curr.next
        
        res = count - n
        
        if count > 2:
            if res == 0:
                return head.next

            else:

                prev = head 
                curr = head.next

                for i in range(res - 1):
                    curr = curr.next
                    prev = prev.next

                prev.next = curr.next
                return head
            
        else:
            if res == 0:
                return head.next
            elif res == 1:
                head.next = None
                return head
            else:
                head = head.next
                return head
        
                
        return head
            
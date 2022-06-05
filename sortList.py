# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        
        
        curr = head
        values = []
        
        while curr is not None:
            values.append(curr.val)
            
            curr = curr.next
            
        values.sort(reverse=True)
        
        root = None
        for i in values:
            newNode = ListNode(i)
            if root is None:
                root = newNode
            else:
                newNode.next = root
                root = newNode
        
        
        return root

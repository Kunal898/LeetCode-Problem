# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = head
        old = head
        while new and new.next:
            old = old.next
            new = new.next.next
        return old
            
        
         

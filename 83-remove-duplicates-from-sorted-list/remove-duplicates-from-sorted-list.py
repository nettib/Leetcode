# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
    
        prev = None
        curr1 = dummy
        curr2 = head
        while curr2:
            if not prev or (prev and curr2.val != prev.val):
                curr1.next = curr2
                curr1 = curr1.next
            prev = curr2
            curr2 = curr2.next

        curr1.next = None
        
        return dummy.next
            
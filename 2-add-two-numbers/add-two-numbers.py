# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        curr = dummy
        stand = 0
        while l1 and l2:
            curr.next = ListNode(((l1.val + l2.val)  + stand) % 10)
            stand = (l1.val + l2.val + stand) // 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            curr.next = ListNode(((l1.val)  + stand) % 10)
            stand = (l1.val + stand) // 10
            curr = curr.next
            l1 = l1.next
        
        while l2:
            curr.next = ListNode(((l2.val)  + stand) % 10)
            stand = (l2.val + stand) // 10
            curr = curr.next
            l2 = l2.next
        
        if stand:
            curr.next = ListNode(stand)
        
        return dummy.next
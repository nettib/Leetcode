# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        count = length - n
        if count == 0:
            head = head.next
            return head

        curr = head
        while count > 1:
            curr = curr.next
            count -=1
        
        curr.next = curr.next.next

        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if not head:
            return head

        spec = curr.next
        temp = curr.next
        count = 0

        while temp:
            curr.next = temp.next
            count += 1
            if count % 2 != 0 and curr.next == None:
                curr.next = spec
                spec = None
            curr = temp
            temp = curr.next
        curr.next = spec
        return head

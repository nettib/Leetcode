# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head
        # prev = None
        # curr = head
        # nex = curr.next

        # while curr:
        #     curr.next = prev
        #     prev = curr
        #     curr = nex
        #     if nex:
        #         nex = nex.next
        
        # head = prev
        # return head
        if not head or not head.next:
            return head
        def reverseLinkedList(prev, curr, nex):
            curr.next = prev
            prev = curr
            if not nex:
                return prev

            return reverseLinkedList(prev, nex, nex.next)
        
        return reverseLinkedList(None, head, head.next)
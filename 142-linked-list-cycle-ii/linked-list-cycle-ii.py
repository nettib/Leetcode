# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        r = head

        while t and r:
            t = t.next
            if r.next:
                r = r.next.next
            elif not r.next: 
                r = None
            if t == r:
                break
        
        if not t or not r:
            return None
        # print(t.val)
        # print(r.val)
        t = head
        while t != r:
            t = t.next
            r = r.next
        
        return t
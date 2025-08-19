# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        c1 = list1
        c2 = list2
        head = None

        if c1 and c2:
            if c1.val <= c2.val:
                head = c1
            else:
                head = c2
        
        elif c1 and not c2:
            head = c1
        elif c2 and not c1:
            head = c2

        while c1 and c2:
            if c1.val <= c2.val:
                if curr:
                    curr.next = c1
                curr = c1
                c1 = c1.next
                
            elif c1.val > c2.val:
                if curr:
                    curr.next = c2
                curr = c2
                c2 = c2.next
        
        while curr and c1:
            curr.next = c1
            curr = c1
            c1 = c1.next

        while curr and c2:
            curr.next = c2
            curr = c2
            c2 = c2.next
                
        
        return head
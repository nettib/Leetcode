# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # print(length)
        temp = head
        prev = None
        for _ in range(length // 2):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
            # print(temp)
        
        head1 = prev
        head2 = temp if length % 2 == 0 else temp.next
        # print(head1, head2)

        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return True
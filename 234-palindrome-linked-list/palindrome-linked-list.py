# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        track = []
        curr = head
        while curr:
            track.append(curr.val)
            curr = curr.next
        
        l, r = 0, len(track) - 1

        while l <= r:
            if track[l] != track[r]:
                return False
            l += 1
            r -= 1
        
        return True
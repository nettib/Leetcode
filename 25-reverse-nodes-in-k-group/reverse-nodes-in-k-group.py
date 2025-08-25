# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevS = dummy

        while True:
            kth = self.getKthNode(prevS, k)
            if not kth:
                break

            nextS = kth.next
            prev, curr = nextS, prevS.next
            while curr != nextS:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevS.next
            prevS.next = prev
            prevS = tmp
        
        return dummy.next
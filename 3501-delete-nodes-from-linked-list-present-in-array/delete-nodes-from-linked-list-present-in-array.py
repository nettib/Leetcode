# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        numsSet = set(nums)

        curr = head
        head1 = head
        prev = None
        while curr:
            if curr.val in numsSet:
                temp = curr.next
                curr.next = None
                if head1 == curr:
                    head1 = temp
                curr = temp
                if prev:
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next
        
        return head1
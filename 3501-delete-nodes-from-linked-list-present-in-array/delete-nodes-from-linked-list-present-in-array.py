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
            if head1.val in numsSet:
                temp = head1.next
                head1.next = None
                head1 = temp
                curr = head1
            elif curr.val in numsSet:
                temp = curr.next
                curr.next = None
                curr = temp
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        
        return head1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        change = curr.next
        while curr.next.next:
            curr.val = change.val
            curr = curr.next
            change = curr.next
        curr.val = change.val
        curr.next = None


        
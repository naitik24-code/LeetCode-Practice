# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
        left=head
        right=prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

        
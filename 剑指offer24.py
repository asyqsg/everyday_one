'''
反转链表
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head

        pre = head
        cur = head.next

        while cur:
            pre.next = cur.next
            cur.next = head
            head = cur
            cur = pre.next
        return head


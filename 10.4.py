'''
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def dfs(l1:ListNode,l2:ListNode,flag):
            if not l1 and not l2 and not flag: return None
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + flag
            node = ListNode(val%10)
            node.next = dfs(l1.next if l1 else None,l2.next if l2 else None,val//10)
            return node
        return dfs(l1,l2,0)










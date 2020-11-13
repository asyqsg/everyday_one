# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class link:
    def demo_link(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node6 = ListNode(6)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        return node1
link = link().demo_link()

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dum1 = node1 = head
        dum2 = node2 = head.next

        while True:
            if node2.next:
                node1.next = node2.next
                node1 = node1.next
            else:
                break

            if node1.next:
                node2.next = node1.next
                node2 = node2.next
            else:
                node2.next = None
                break
        node1.next = dum2
        return head

if __name__ == '__main__':
    b = Solution().oddEvenList(link)

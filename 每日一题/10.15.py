"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        deque = [root]
        res = []

        while deque:
            cur = []
            nextlayer = []
            for node in deque:
                cur.append(node)
                if node.left:
                    nextlayer.append(node.left)
                if node.right:
                    nextlayer.append(node.right)
            deque = nextlayer
            res.append(cur)
        for line in cur:
            size = len(line)
            if size == 1:
                line[0].next = None
            else:
                for i in range(1,size):
                    line[i-1].next = line[i]
                line[i].next = None

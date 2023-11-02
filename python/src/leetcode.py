from collections import deque
from typing import Generator


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order_insert(self, val):
        q = deque()
        q.append(self)
        while True:
            p = q.popleft()

            if not p.left:
                p.left = TreeNode(val)
                return

            if not p.right:
                p.right = TreeNode(val)
                return

            q.append(p.left)
            q.append(p.right)

    def level_order_traversal(self) -> Generator:
        q = deque()
        q.append(self)
        while q:
            p = q.popleft()
            yield p.val

            if p.left:
                q.append(p.left)

            if p.right:
                q.append(p.right)

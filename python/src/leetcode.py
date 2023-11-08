from collections import deque
from typing import Generator, List, Optional


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


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    q = deque()
    q.append(root)

    i = 1
    while i < len(values):
        p = q.popleft()

        if values[i] is not None:
            p.left = TreeNode(values[i])
            q.append(p.left)
        i += 1

        if i < len(values) and values[i] is not None:
            p.right = TreeNode(values[i])
            q.append(p.right)
        i += 1

    return root

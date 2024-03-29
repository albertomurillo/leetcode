from __future__ import annotations

from collections import deque
from typing import Deque, Generator, Iterable, List, Optional


# Definition of Interval:
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Optional[Node] = None, random: Optional[Node] = None
    ):
        self.val = x
        self.next = next
        self.random = random


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order_traversal(self) -> Generator:
        q: Deque[TreeNode] = deque()
        q.append(self)
        while q:
            p = q.popleft()
            yield p.val

            if p.left:
                q.append(p.left)

            if p.right:
                q.append(p.right)


def build_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    dummy = ListNode()
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def iter_list(head: Optional[ListNode]) -> Iterable[int]:
    if not head:
        return
    cur = head
    while cur:
        yield cur.val
        cur = cur.next


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    q: Deque[TreeNode] = deque()
    q.append(root)

    i = 1
    while i < len(values):
        p = q.popleft()

        if (val := values[i]) is not None:
            p.left = TreeNode(val)
            q.append(p.left)
        i += 1

        if i < len(values) and (val := values[i]) is not None:
            p.right = TreeNode(val)
            q.append(p.right)
        i += 1

    return root

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


# Definition of Interval:
class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Node | None = None, random: Node | None = None
    ) -> None:
        self.val = x
        self.next = next
        self.random = random


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def level_order_traversal(self) -> Generator:
        q: deque[TreeNode] = deque()
        q.append(self)
        while q:
            p = q.popleft()
            yield p.val

            if p.left:
                q.append(p.left)

            if p.right:
                q.append(p.right)


def build_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    dummy = ListNode()
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def iter_list(head: ListNode | None) -> Iterable[int]:
    if not head:
        return
    cur = head
    while cur:
        yield cur.val
        cur = cur.next


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    q: deque[TreeNode] = deque()
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

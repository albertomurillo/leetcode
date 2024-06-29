# https://leetcode.com/problems/lru-cache


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache: dict[int, Node] = {}
        self._left = Node(0, 0)
        self._right = Node(0, 0)
        self._left.next = self._right
        self._right.prev = self._left

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._remove(node)
        self._append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._remove(self._cache[key])

        node = Node(key, value)
        self._append(node)
        self._cache[key] = node

        if len(self._cache) > self._capacity:
            lru = self._left.next
            assert lru
            self._remove(lru)
            del self._cache[lru.key]

    def _append(self, node: Node) -> None:
        tmp = self._right.prev
        assert tmp
        self._right.prev = node
        node.next = self._right
        node.prev = tmp
        tmp.next = node

    def _remove(self, node: Node) -> None:
        assert node.next
        assert node.prev
        node.next.prev = node.prev
        node.prev.next = node.next

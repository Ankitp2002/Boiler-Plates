class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be > 0")

        self.capacity = capacity
        self._cache = {}

        self._head = _Node()
        self._tail = _Node()

        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove_node(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: _Node) -> None:
        first = self._head.next

        node.prev = self._head
        node.next = first

        self._head.next = node
        first.prev = node

    def _move_to_front(self, node: _Node) -> None:
        self._remove_node(node)
        self._add_to_front(node)

    def _evict_lru(self) -> None:
        lru = self._tail.prev
        if lru is self._head:
            return

        self._remove_node(lru)
        del self._cache[lru.key]

    def get(self, key):
        node = self._cache.get(key)
        if not node:
            return -1

        self._move_to_front(node)
        return node.value

    def put(self, key, value) -> None:
        node = self._cache.get(key)

        if node:
            node.value = value
            self._move_to_front(node)
            return

        if len(self._cache) >= self.capacity:
            self._evict_lru()

        node = _Node(key, value)
        self._cache[key] = node
        self._add_to_front(node)

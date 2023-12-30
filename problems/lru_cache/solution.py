class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            
            # Move the accessed node to the end
            self._remove_node(node)
            self._add_to_tail(node)

            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            # If the key is already present, update the value and move the node to the end
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is full, remove the least recently used item (the first item)
                oldest = self.head.next
                self._remove_node(oldest)
                del self.cache[oldest.key]

            # Add the new key-value pair to the cache and to the end of the linked list
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
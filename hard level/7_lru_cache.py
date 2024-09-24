class Node:
    def __init__(self, key, val, right=None, left=None):
        self.key = key
        self.val = val
        self.right = right
        if right:
            right.left = self
        self.left = left
        if left:
            left.right = self

    def link(self, right=None, left=None):
        if right:
            self.right = right
            right.left = self
        if left:
            self.left = left
            left.right = self


class DoublyLinkedList:
    def __init__(self):
        self.start = Node(None, None)
        self.end = Node(None, None, left=self.start)

    def add(self, key, val):
        node = Node(key, val, self.end, self.end.left)
        return node

    def pop(self):
        key = self.start.right.key
        self.start.link(self.start.right.right)
        return key

    def up(self, node):
        node.right.left = node.left
        node.left.right = node.right
        node.link(self.end, self.end.left)


class LRUCache:

    def __init__(self, capacity: int):
        self.n = 0
        self.capacity = capacity
        self.data = {}
        self.linkedlist = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.data:
            self.linkedlist.up(self.data[key])
            return self.data[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.linkedlist.up(self.data[key])
            self.data[key].val = value
            return
        if self.capacity > self.n:
            node = self.linkedlist.add(key, value)
            self.data[key] = node
            self.n += 1
            return
        key_ = self.linkedlist.pop()
        del self.data[key_]
        node = self.linkedlist.add(key, value)
        self.data[key] = node


a = ["LRUCache","put","put","get","put","get","put","get","get","get"]
b = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

lru = None
result = []
for i in range(len(a)):
    if a[i] == "LRUCache":
        lru = LRUCache(b[i][0])
        result.append(None)
    if a[i] == "put":
        result.append(lru.put(b[i][0],b[i][1])  )
    if a[i] == "get":
        result.append(lru.get(b[i][0]))

print(result)

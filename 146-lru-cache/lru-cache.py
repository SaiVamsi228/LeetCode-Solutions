class Node:

    def __init__(self,key,value):
        
        self.key = key

        self.val = value

        self.prev = None

        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        self.cache = {}

        self.head = Node(-1,-1)

        self.tail = Node(-1,-1)
        
        self.head.next = self.tail

        self.tail.prev = self.head
    
    def remove(self,node):

        node.next.prev = node.prev

        node.prev.next = node.next
    
    def add(self,node):

        node.next = self.head.next

        node.prev = self.head

        self.head.next = node

        node.next.prev = node
    
    def get(self,key):

        if key in self.cache:

            node = self.cache[key]

            self.remove(node)

            self.add(node)

            return node.val

        return -1        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:

            node = self.cache[key]

            self.remove(node)

            node.val = value

        else:

            if len(self.cache) == self.capacity :

                node = self.tail.prev
                
                del self.cache[node.key]

                self.remove(node)

        node = Node(key,value)

        self.add(node)

        self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
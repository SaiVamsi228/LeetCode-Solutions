from collections import defaultdict, deque
class Node:
    def __init__(self,key,val,freq = 1):
        self.key = key
        self.val = val
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_list = defaultdict(deque)
        self.freq_to_key = defaultdict(set)
        self.min_freq = 0

    def get(self, key: int) -> int:

        if key not in self.key_to_node:
            return -1   
        else:
            node = self.key_to_node[key]
            self.touch(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.touch(node)
            return
        if len(self.key_to_node) == self.capacity:
            # need to evict lfu
            key_to_be_removed = self.freq_to_list[self.min_freq].popleft()
            self.freq_to_key[self.min_freq].discard(key_to_be_removed)
            del self.key_to_node[key_to_be_removed]
        
        # creating new_ele
        self.min_freq = 1
        self.freq_to_list[1].append(key)
        self.freq_to_key[1].add(key)          
        new_node = Node(key,value,1)
        self.key_to_node[key] = new_node
    
    def touch(self,node):

        prev_freq = node.freq
        new_freq = prev_freq + 1
        node.freq = new_freq
        
        # removing stale values
        self.freq_to_list[prev_freq].remove(node.key)
        self.freq_to_key[prev_freq].discard(node.key)

        if len(self.freq_to_list[prev_freq]) == 0:
            del self.freq_to_list[prev_freq]
            del self.freq_to_key[prev_freq]
            if prev_freq == self.min_freq:
                self.min_freq += 1

        # creating new values
        if new_freq not in self.freq_to_list:
            new_list = deque()
            new_set = set()
            self.freq_to_list[new_freq] = new_list
            self.freq_to_key[new_freq] = new_set

        self.freq_to_list[new_freq].append(node.key)
        self.freq_to_key[new_freq].add(node.key)
        node.freq = new_freq


        



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
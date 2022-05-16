TITLE = 'LRU Cache'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 2614 ms, faster than 7.86%
    Memory Usage: 75 MB, less than 82.38%
'''

class LRUCache:

    def __init__(self, capacity: int):
        self.queue = []
        self.existing_keys = set()
        self.pairs = dict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.existing_keys:
            self.queue.pop(self.queue.index(key))
            self.queue.append(key)
            return self.pairs[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.existing_keys:
            self.existing_keys.add(key)
            self.queue.append(key)
            self.pairs[key] = value
            if len(self.queue) > self.cap:
                old_key = self.queue.pop(0)
                self.existing_keys.remove(old_key)
                del self.pairs[old_key]
                
        else:
            self.queue.pop(self.queue.index(key))
            self.queue.append(key)
            self.pairs[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
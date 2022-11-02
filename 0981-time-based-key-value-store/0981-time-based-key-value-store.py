from collections import defaultdict as ddict
import heapq

class TimeMap:

    def __init__(self):
        self.data = ddict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.data[key], [timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]
        for idx in range(len(data)-1, -1, -1):
            item = data[idx]
            if item[0] <= timestamp:
                return item[1]
            
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
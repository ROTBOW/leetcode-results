from heapq import heappush, heappop
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = list()
        unq = Counter(arr)

        for key, v in unq.items():
            heappush(heap, (v, key))

        while k > 0 and heap:
            if k >= heap[0][0]:
                k -= heappop(heap)[0]
            else:
                break

        return len(heap)

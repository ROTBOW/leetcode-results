from heapq import heappush, heappop

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = list()

        for i in range(len(mat)):
            row = mat[i]
            heappush(heap, (row.count(1), i))

        return [heappop(heap)[1] for _ in range(k)]
        